"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Gear, GearType, Manufacturer, Specification, Review

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

        if "gear_type" in request.query_params:
            gear = gear.filter(gear_type__id = request.query_params['specifications']['gear_type']['id'])

        serializer = GearSerializer(gear, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        manufacturer = Manufacturer.objects.get(pk=request.data['specifications']['manufacturer'])
        gear_types = GearType.objects.get(pk=request.data['specifications']['gear_types'])
        specifications = Specification.objects.create(
            release_date = request.data['specifications']["release_date"],
            manufacturer = manufacturer,
            gear_types = gear_types,
            number_of_keys = request.data['specifications']['number_of_keys'],
            voices = request.data['specifications']['voices'],
            arpeggiator = request.data['specifications']['arpeggiator'],
            sequencer = request.data['specifications']['sequencer'],
            velocity = request.data['specifications']['velocity'],
            aftertouch = request.data['specifications']['aftertouch']
        )

        gear = Gear.objects.create(
            name=request.data["name"],
            image=request.data["image"],
            price=request.data["price"],
            description=request.data["description"],
            specifications = specifications
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

        manufacturer = Manufacturer.objects.get(pk=request.data['specifications']['manufacturer'])
        gear_types = GearType.objects.get(pk=request.data['specifications']['gear_types'])

        specifications = Specification.objects.get(pk=pk)
        specifications.release_date = request.data['specifications']["release_date"]
        specifications.manufacturer = manufacturer
        specifications.gear_types = gear_types
        specifications.number_of_keys = request.data['specifications']["number_of_keys"]
        specifications.voices = request.data['specifications']["voices"]
        specifications.arpeggiator = request.data['specifications']["arpeggiator"]
        specifications.sequencer = request.data['specifications']["sequencer"]
        specifications.velocity = request.data['specifications']["velocity"]
        specifications.aftertouch = request.data['specifications']["aftertouch"]

        specifications.save()
        gear.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        


    def destroy(self, request, pk):
        gear = Gear.objects.get(pk=pk)

        gear.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GearSpecificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specification
        fields = ('release_date', 'manufacturer', 'gear_types', 'number_of_keys', 'voices', 'arpeggiator', 'sequencer', 'velocity', 'aftertouch')

class GearReviewSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Review
        fields = ('id','waver_user', 'review', 'rating', 'created_on')
        depth = 2

class GearSerializer(serializers.ModelSerializer):

    reviews = GearReviewSerializer(many=True)

    class Meta: 
        model = Gear
        fields = ('id', 'name', 'image', 'price', 'description', "specifications", "reviews" )
        depth = 2
