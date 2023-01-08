"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Gear, GearType, Manufacturer, Specification, Review
from rest_framework.decorators import action



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

        if "gear_types" in request.query_params:
            gear_types_id = request.query_params['gear_types']
            gear = gear.filter(specifications__gear_types__id=gear_types_id)

        if "name" in request.query_params:
            name = request.query_params['name']
            gear = gear.filter(name__contains=name)


        serializer = GearSerializer(gear, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        manufacturer = Manufacturer.objects.get(pk=request.data['manufacturer'])
        gear_types = GearType.objects.get(pk=request.data['gear_types'])
        specifications = Specification.objects.create(
            release_date = request.data["release_date"],
            manufacturer = manufacturer,
            gear_types = gear_types,
            number_of_keys = request.data['number_of_keys'],
            voices = request.data['voices'],
            arpeggiator = request.data['arpeggiator'],
            sequencer = request.data['sequencer'],
            velocity = request.data['velocity'],
            aftertouch = request.data['aftertouch']
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

        manufacturer = Manufacturer.objects.get(pk=request.data['manufacturer'])
        gear_types = GearType.objects.get(pk=request.data['gear_types'])

        specifications = Specification.objects.get(pk=pk)
        specifications.release_date = request.data["release_date"]
        specifications.manufacturer = manufacturer
        specifications.gear_types = gear_types
        specifications.number_of_keys = request.data["number_of_keys"]
        specifications.voices = request.data["voices"]
        specifications.arpeggiator = request.data["arpeggiator"]
        specifications.sequencer = request.data["sequencer"]
        specifications.velocity = request.data["velocity"]
        specifications.aftertouch = request.data["aftertouch"]

        specifications.save()
        gear.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        


    def destroy(self, request, pk):
        gear = Gear.objects.get(pk=pk)
        # specifications = Specification.objects.get(pk=pk)

        gear.delete()
        # specifications.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class GearSpecificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specification
        fields = ('release_date', 'manufacturer', 'gear_types', 'number_of_keys', 'voices', 'arpeggiator', 'sequencer', 'velocity', 'aftertouch')

class GearSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Gear
        fields = ('id', 'name', 'image', 'price', 'description', "specifications", "reviews", "average_rating" )
        depth = 3
