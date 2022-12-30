"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import UsedGear, WaverUser
from rest_framework.decorators import action



class UsedGearView(ViewSet):

    
    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        
        used_gear = UsedGear.objects.get(pk=pk)
        serializer = UsedGearSerializer(used_gear)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        used_gear = UsedGear.objects.all()
        serializer = UsedGearSerializer(used_gear, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        waver_user = WaverUser.objects.get(pk = request.auth.user.id)
        used_gear = UsedGear.objects.create(
            waver_user = waver_user,
            item = request.data['item'],
            image = request.data['image'],
            price = request.data['price'],
            details = request.data['details']
        )
        serializer = UsedGearSerializer(used_gear)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """


        used_gear = UsedGear.objects.get(pk=pk)
        used_gear.item = request.data["item"]
        used_gear.image = request.data["image"]
        used_gear.price = request.data["price"]
        used_gear.details = request.data["details"]

        used_gear.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        


    def destroy(self, request, pk):
        used_gear = UsedGear.objects.get(pk=pk)

        used_gear.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UsedGearSerializer(serializers.ModelSerializer):

    class Meta: 
        model = UsedGear
        fields = ('id', 'waver_user', 'item', 'image', 'price', 'details')
        depth = 2
