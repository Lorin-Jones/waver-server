"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Gear, GearType, Manufacturer

class GearView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        gear = Gear.objects.get(pk=pk)
        serializer = GearSerializer(gear)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        gear = Gear.objects.all()
        serializer = GearSerializer(gear, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gear_type = GearType.objects.get(pk=request.data["gear_type"])
        manufacturer = Manufacturer.objects.get(pk=request.data["manufacturer"])


        gear = Gear.objects.create(
            name=request.data["name"],
            image=request.data["image"],
            price=request.data["price"],
            description=request.data["description"],
            release_date=request.data["release_date"],
            manufacturer=manufacturer,
            gear_type=gear_type

            
        )
        serializer = GearSerializer(gear)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        gear = Gear.objects.get(pk=pk)
        gear.name = request.data["name"]
        gear.image = request.data["image"]
        gear.price = request.data["price"]
        gear.description = request.data["description"]
        gear.release_date = request.data["release_date"]



        manufacturer = Manufacturer.objects.get(pk=request.data["manufacturer"])
        gear.manufacturer = manufacturer
        gear_type = GearType.objects.get(pk=request.data["gear_type"])
        gear.gear_type = gear_type
        gear.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        gear = Gear.objects.get(pk=pk)
        gear.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GearSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Gear
        fields = ('id', 'name', 'image', 'price', 'description', "release_date", "manufacturer", "gear_type", )
        depth = 2