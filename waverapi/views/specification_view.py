"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Specification

class SpecificationView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        specification = Specification.objects.get(pk=pk)
        serializer = SpecificationSerializer(specification)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        specification = Specification.objects.all()
        serializer = SpecificationSerializer(specification, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        specification = Specification.objects.create(
            description=request.data["description"]
        )
        serializer = SpecificationSerializer(specification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SpecificationSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Specification
        fields = ('id', 'description', )
        