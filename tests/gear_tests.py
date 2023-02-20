import json
from rest_framework import status
from rest_framework.test import APITestCase
from waverapi.models import Gear, WaverUser, Manufacturer, GearType, Specification
from rest_framework.authtoken.models import Token


class GearTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'waver_users', 'gear', 'gear_types', 'manufacturers', 'specifications']

    def setUp(self):
        self.waver_user = WaverUser.objects.first()
        token = Token.objects.get(user=self.waver_user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        self.manufacturer = Manufacturer.objects.create(
            name='test manufacturer',
        )
        self.gear_type = GearType.objects.create(
            name='test gear_type',
        )
        self.specifications = Specification.objects.create(
            release_date = 2011,
            manufacturer = self.manufacturer,
            gear_types = self.gear_type,
            number_of_keys = "test",
            voices = "test",
            arpeggiator = False,
            sequencer = False,
            velocity = False,
            aftertouch = False
        )
       



    def test_create_gear(self):
        """
        Ensure we can create a new gear.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/gear"

        # Define the request body
        data = {
            "name": "OpSix",
            "image": "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg",
            "price": 749,
            "description": "opsix is a digital synth unlike any other, with sounds to match. Instantly explore hundreds of fresh, cutting-edge sounds to inspire your next musical project! Go even further with the power of customization right at your fingertips. Front panel colored controls provide easy access for dramatic shifts in sound characteristics, from icy, sparkling chimes to fuzzy, deep basses. The opsix is an entirely new tool that reveals a world of frequency exploration and a wide range of dynamic possibilities.",
            "release_date": 2021,
            "number_of_keys": "61-Key",
            "voices": "6-Voices",
            "arpeggiator": True,
            "sequencer": True,
            "velocity": True,
            "aftertouch": True,
            "manufacturer": 1,
            "gear_types": 1
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the gear was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["name"], "OpSix")
        self.assertEqual(json_response["image"], "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg")
        self.assertEqual(json_response["price"], 749)
        self.assertEqual(json_response["description"], "opsix is a digital synth unlike any other, with sounds to match. Instantly explore hundreds of fresh, cutting-edge sounds to inspire your next musical project! Go even further with the power of customization right at your fingertips. Front panel colored controls provide easy access for dramatic shifts in sound characteristics, from icy, sparkling chimes to fuzzy, deep basses. The opsix is an entirely new tool that reveals a world of frequency exploration and a wide range of dynamic possibilities.")
        self.assertEqual(json_response['specifications']["release_date"], 2021)
        self.assertEqual(json_response['specifications']["number_of_keys"], "61-Key")
        self.assertEqual(json_response['specifications']["voices"], "6-Voices")
        self.assertEqual(json_response['specifications']["arpeggiator"], True)
        self.assertEqual(json_response['specifications']["sequencer"], True)
        self.assertEqual(json_response['specifications']["velocity"], True)
        self.assertEqual(json_response['specifications']["aftertouch"], True)





    def test_get_gear(self):
        """
        Ensure we can get an existing game.
        """

        # Seed the database with a game
        gear = Gear()
        gear.name = "Minilogue"
        gear.image = "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg"
        gear.price = 399
        gear.description = "Meet minilogue; the stylish, innovative, 37 slim-key fully programmable analog polyphonic synthesizer."
        gear.specifications = self.specifications
        gear.save()
        

        # Initiate request and store response
        response = self.client.get(f"/gear/{gear.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["name"], "Minilogue")
        self.assertEqual(json_response["image"], "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg")
        self.assertEqual(json_response["price"], 399)
        self.assertEqual(json_response["description"], "Meet minilogue; the stylish, innovative, 37 slim-key fully programmable analog polyphonic synthesizer.")
        

    def test_change_gear(self):
        """
        Ensure we can change an existing game.
        """
        gear = Gear()
        gear.name = "Minilogue"
        gear.image = "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg"
        gear.price = 399
        gear.description = "Meet minilogue; the stylish, innovative, 37 slim-key fully programmable analog polyphonic synthesizer."
        gear.specifications = self.specifications
        gear.save()

        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "name": "Oopsie",
            "image": "an image",
            "price": 499,
            "description": "some text",
            "release_date": 2017,
            "number_of_keys": "32-Key",
            "voices": "4-Voices",
            "arpeggiator": False,
            "sequencer": True,
            "velocity": False,
            "aftertouch": True,
            "manufacturer": 2,
            "gear_types": 2
            
        }

        response = self.client.put(f"/gear/{gear.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET game again to verify changes were made
        response = self.client.get(f"/gear/{gear.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["name"], "Oopsie")
        self.assertEqual(json_response["image"], "an image")
        self.assertEqual(json_response["price"], 499)
        self.assertEqual(json_response["description"], "some text")
        self.assertEqual(json_response['specifications']["release_date"], 2017)
        self.assertEqual(json_response['specifications']["number_of_keys"], "32-Key")
        self.assertEqual(json_response['specifications']["voices"], "4-Voices")
        self.assertEqual(json_response['specifications']["arpeggiator"], False)
        self.assertEqual(json_response['specifications']["sequencer"], True)
        self.assertEqual(json_response['specifications']["velocity"], False)
        self.assertEqual(json_response['specifications']["aftertouch"], True)


    def test_delete_gear(self):
        """
        Ensure we can delete an existing gear.
        """
       


    

        gear = Gear()
        gear.name = "Minilogue"
        gear.image = "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg"
        gear.price = 399
        gear.description = "Meet minilogue; the stylish, innovative, 37 slim-key fully programmable analog polyphonic synthesizer."
        gear.specifications = self.specifications
        gear.save()

        # DELETE the gear you just created
        response = self.client.delete(f"/gear/{gear.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the gear again to verify you get a 404 response
        response = self.client.get(f"/gear/{gear.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       
       
       