"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import GearType

class GearTypeView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        gear_type = GearType.objects.get(pk=pk)
        serializer = GearTypeSerializer(gear_type)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        gear_type = GearType.objects.all()
        serializer = GearTypeSerializer(gear_type, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gear_type = GearType.objects.create(
            name=request.data["name"]
        )
        serializer = GearTypeSerializer(gear_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GearTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = GearType
        fields = ('id', 'name', )
        