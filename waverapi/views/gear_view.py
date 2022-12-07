"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Gear

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

    def destroy(self, request, pk):
        gear = Gear.objects.get(pk=pk)
        gear.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GearSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Gear
        fields = ('id', 'name', 'image', 'price', 'description', "release_date", "manufacturer", "gear_type", )
        depth = 2