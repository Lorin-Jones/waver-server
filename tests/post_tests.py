import json
from rest_framework import status
from rest_framework.test import APITestCase
from waverapi.models import Post, WaverUser
from rest_framework.authtoken.models import Token

class PostTests(APITestCase):

    fixtures = ['posts', 'waver_users', 'users', 'tokens']

    def setUp(self):
        self.waver_user = WaverUser.objects.first()
        token = Token.objects.get(user=self.waver_user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        

    def test_create_post(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/posts"
        
        data = {
            "user": 1,
            "image": "asdfwefd",
            "title": "test title",
            "content": "test content",
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties are correct
        self.assertEqual(json_response["image"], "asdfwefd")
        self.assertEqual(json_response["title"], "test title")
        self.assertEqual(json_response["content"], "test content")


    def test_get_posts(self):
        """
        Ensure we can get an existing game.
        """

        # Seed the database with a game
        post = Post()
        post.user = self.waver_user
        post.image = "test image"
        post.title = "test title"
        post.publication_date = "2022-12-06"
        post.content = "test content"
        post.save()
        

        # Initiate request and store response
        response = self.client.get(f"/posts/{post.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["image"], "test image")
        self.assertEqual(json_response["title"], "test title")
        self.assertEqual(json_response["publication_date"], "2022-12-06")
        self.assertEqual(json_response["content"], "test content")

    def test_change_posts(self):
        """
        Ensure we can change an existing game.
        """
        post = Post()
        post.user = self.waver_user
        post.image = "test image"
        post.title = "test title"
        post.publication_date = "2022-01-05"
        post.content = "test content"
        post.save()

        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "image": "new image",
            "title": "new title",
            "content": "new content",
        }

        response = self.client.put(f"/posts/{post.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET game again to verify changes were made
        response = self.client.get(f"/posts/{post.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["image"], "new image")
        self.assertEqual(json_response["title"], "new title")
        self.assertEqual(json_response["content"], "new content")
       
    
    # def test_delete_gear(self):
        
    #     post = Post()
    #     post.user = self.waver_user
    #     post.image = "test image"
    #     post.title = "test title"
    #     post.publication_date = "2022-01-05"
    #     post.content = "test content"
    #     post.save()

    #     # DELETE the gear you just created
    #     response = self.client.delete(f"/posts/{post.id}")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # GET the post again to verify you get a 404 response
    #     response = self.client.get(f"/posts/{post.id}")
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       
       
       