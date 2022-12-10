"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Manufacturer

class ManufacturerView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        manufacturer = Manufacturer.objects.get(pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        manufacturer = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturer, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        manufacturer = Manufacturer.objects.create(
            name=request.data["name"],   
        )
        
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer.name = request.data["name"]

        manufacturer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Manufacturer
        fields = ('id', 'name' )
        