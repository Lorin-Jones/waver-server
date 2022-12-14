"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from waverapi.models import Review, Gear, Review, WaverUser
from datetime import date



class ReviewView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types
        

        Returns:
            Response -- JSON serialized list of game types
        """
        reviews = Review.objects.all()

        # if "gear" in request.query_params:
        #     reviews = reviews.filter(gear__id = request.query_params['gear'])

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        required_fields = ['gear', 'review', 'rating']
        missing_fields = 'Hey! You are missing'
        is_field_missing = False

        for field in required_fields:
            value = request.data.get(field, None)
            if value is None:
                missing_fields = f'{missing_fields} {field}'
                is_field_missing = True

        if is_field_missing:
            return Response({"message": missing_fields}, status = status.HTTP_400_BAD_REQUEST)

        try:
            assigned_gear = Gear.objects.get(pk=request.data['gear'])
        except Gear.DoesNotExist:
            return Response({"message": "The gear you specified does not exist"}, status = status.HTTP_404_NOT_FOUND)

        waver_user = WaverUser.objects.get(pk=request.auth.user.id)
        review = Review()
        review.waver_user = waver_user
        review.gear = assigned_gear
        review.review = request.data['review']
        review.rating = request.data['rating']
        review.created_on = date.today()

        review.save()


        serializer = ReviewSerializer(review)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        reveiws = Review.objects.get(pk=pk)
        reveiws.review = request.data["review"]
        reveiws.rating = request.data['rating']
        

        
        reveiws.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

       


    def destroy(self, request, pk=None):
        """Handle DELETE requests for waver_users

        Returns:
            Response: None with 204
        """
        review = Review.objects.get(pk=pk)
        
        review.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ReviewSerializer(serializers.ModelSerializer):


    class Meta: 
        model = Review
        fields = ('id', 'waver_user', 'gear', 'review', 'rating', 'created_on' )
        depth = 2
        