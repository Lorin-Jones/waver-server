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
            description='test specifications'
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
            "release_date": 2020,
            "manufacturer": 1,
            "gear_type": 1,
            "specifications": [1,2,3]
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
        self.assertEqual(json_response["release_date"], 2020)
       
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
        gear.release_date = 2016
        gear.manufacturer_id = 1
        gear.gear_type_id = 2
        gear.save()
        gear.specifications.add(1)
        gear.specifications.add(2)
        gear.specifications.add(3)

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
        self.assertEqual(json_response["release_date"], 2016)

    # def test_change_gear(self):
    #     """
    #     Ensure we can change an existing game.
    #     """
    #     gear = Gear()
    #     gear.name = "Minilogue"
    #     gear.image = "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg"
    #     gear.price = 399
    #     gear.description = "Meet minilogue; the stylish, innovative, 37 slim-key fully programmable analog polyphonic synthesizer."
    #     gear.release_date = 2016
    #     gear.manufacturer_id = 1
    #     gear.gear_type_id = 2
    #     gear.save()

    #     # DEFINE NEW PROPERTIES FOR GAME
    #     data = {
    #         "name": "OpSix",
    #         "image": "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg",
    #         "price": 749,
    #         "description": "opsix is a digital synth unlike any other, with sounds to match. Instantly explore hundreds of fresh, cutting-edge sounds to inspire your next musical project! Go even further with the power of customization right at your fingertips. Front panel colored controls provide easy access for dramatic shifts in sound characteristics, from icy, sparkling chimes to fuzzy, deep basses. The opsix is an entirely new tool that reveals a world of frequency exploration and a wide range of dynamic possibilities.",
    #         "release_date": 2020,
    #         "manufacturer": 2,
    #         "gear_type": 1,
            
    #     }

    #     response = self.client.put(f"/gear/{gear.id}", data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # GET game again to verify changes were made
    #     response = self.client.get(f"/gear/{gear.id}")
    #     json_response = json.loads(response.content)

    #     # Assert that the properties are correct
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(json_response["name"], "OpSix")
    #     self.assertEqual(json_response["image"], "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg")
    #     self.assertEqual(json_response["price"], 749)
    #     self.assertEqual(json_response["description"], "opsix is a digital synth unlike any other, with sounds to match. Instantly explore hundreds of fresh, cutting-edge sounds to inspire your next musical project! Go even further with the power of customization right at your fingertips. Front panel colored controls provide easy access for dramatic shifts in sound characteristics, from icy, sparkling chimes to fuzzy, deep basses. The opsix is an entirely new tool that reveals a world of frequency exploration and a wide range of dynamic possibilities.")
    #     self.assertEqual(json_response["release_date"], 2020)

    # def test_delete_gear(self):
    #     """
    #     Ensure we can delete an existing gear.
    #     """
    #     gear = Gear()
    #     gear.name = "Minilogue"
    #     gear.image = "https://res.cloudinary.com/dlr2tm7qr/image/upload/v1670526920/Waver/Gear%20Images/opsix_k7ojgc.jpg"
    #     gear.price = 399
    #     gear.description = "Meet minilogue; the stylish, innovative, 37 slim-key fully programmable analog polyphonic synthesizer."
    #     gear.release_date = 2016
    #     gear.manufacturer_id = 1
    #     gear.gear_type_id = 2
    #     gear.save()

    #     # DELETE the gear you just created
    #     response = self.client.delete(f"/gear/{gear.id}")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # GET the gear again to verify you get a 404 response
    #     response = self.client.get(f"/gear/{gear.id}")
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)