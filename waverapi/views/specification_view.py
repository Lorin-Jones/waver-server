"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Specifications, Manufacturer, GearType

class SpecificationView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        specifications = Specifications.objects.get(pk=pk)
        serializer = SpecificationSerializer(specifications)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        specifications = Specifications.objects.all()
        serializer = SpecificationSerializer(specifications, many=True)
        return Response(serializer.data)   

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        manufacturer = Manufacturer.objects.get(pk=request.data['manufacturer'])
        gear_types = GearType.objects.get(pk=request.data['gear_types'])

        specifications = Specifications.objects.get(pk=pk)
        specifications.release_date = request.data["release_date"]
        specifications.manufacturer = manufacturer
        specifications.gear_types = gear_types
        specifications.voices = request.data["voices"]
        specifications.arpeggiator = request.data["arpeggiator"]
        specifications.sequencer = request.data["sequencer"]
        specifications.velocity = request.data["velocity"]
        specifications.aftertouch = request.data["aftertouch"]

        
        specifications.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for waver_users

        Returns:
            Response: None with 204
        """
        review = Specifications.objects.get(pk=pk)
        
        review.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SpecificationSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Specifications
        fields = ('id', 'release_date', 'manufacturer', 'gear_types', 'number_of_keys', 'voices', 'arpeggiator', 'sequencer', 'velocity', 'aftertouch' )
        