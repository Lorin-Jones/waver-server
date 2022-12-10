import json
from rest_framework import status
from rest_framework.test import APITestCase
from waverapi.models import Gear, WaverUser, Manufacturer, GearType
from rest_framework.authtoken.models import Token


class GearTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'waver_users', 'gear', 'gear_types', 'manufacturers']

    def setUp(self):
        self.waver_user = WaverUser.objects.first()
        token = Token.objects.get(user=self.waver_user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        self.manufacturer = Manufacturer.objects.create(
            name='test manufacturer',
        )
        self.gear_type = GearType.objects.create(
            name='test manufacturer',
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
            "manufacturer": self.manufacturer.id,
            "gear_type": 1
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
        self.assertEqual(json_response["manufacturer"], 1)
        self.assertEqual(json_response["gear_type"], 1)