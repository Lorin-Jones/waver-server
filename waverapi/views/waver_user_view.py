"""View module for handling requests for user data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import WaverUser
from django.contrib.auth.models import User


class WaverUserView(ViewSet):
    """Lightning Raccoons API users view"""

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """

        users = WaverUser.objects.all()
        serialized = WaverUserSerializer(users, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user record
        """

        user = WaverUser.objects.get(pk=pk)
        serialized = WaverUserSerializer(user, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
            """Handle PUT requests for a game

            Returns:
                Response -- Empty body with 204 status code
            """
            
            user = User.objects.get(pk=pk)
            user.username = request.data["username"]
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            user.email = request.data["last_name"]
            user.is_staff = request.data["is_staff"]

            user.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', )

class WaverUserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    user = UserSerializer(many=False)
    
    class Meta:
        model = WaverUser
        fields = ( 'id', 'user', 'bio', )
