"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models.post import Post
from waverapi.models.waver_user import WaverUser
from django.contrib.auth.models import User

from datetime import date


class PostView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = WaverUser.objects.get(pk=request.auth.user.id)
        post = Post.objects.create(
            user = user,
            image = request.data['image'],
            title = request.data['title'],
            publication_date = date.today(),
            content = request.data['content']  
        )
        
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.image = request.data["image"]
        post.content = request.data['content']

        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class PostWaverUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaverUser
        fields = ( 'user', 'full_name')
        

class PostSerializer(serializers.ModelSerializer):

    user = PostWaverUserSerializer(many=False)

    class Meta: 
        model = Post
        fields = ('id', 'user', 'image', 'title', 'publication_date', 'content' )
