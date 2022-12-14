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

        if "gear" in request.query_params:
            reviews = reviews.filter(gear__id = request.query_params['gear'])

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)   

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        required_fields = ['gearId', 'review']
        missing_fields = "Oops! It looks like you're missing a field!"
        is_field_missing = False

        for field in required_fields:
            value = request.data.get(field, None)
            if value is None:
                missing_fields = f'{missing_fields} and {field}'
                is_field_missing = True

        if is_field_missing:
            return Response({"message": missing_fields}, status = status.HTTP_400_BAD_REQUEST)

        try:
            assigned_gear = Gear.objects.get(pk=request.data['gearId'])
        except Gear.DoesNotExist:
            return Response({"message": "The gear you specified does not exist"}, status = status.HTTP_404_NOT_FOUND)

        waver_user = WaverUser.objects.get(pk = request.auth.user.pk)
        review = Review()
        review.waver_user = waver_user
        review.gear = assigned_gear
        review.review = request.data['review']
        review.created_on = date.today()
        review.save()


        serializer = ReviewSerializer(review)
        return Response(serializer.data, status = status.HTTP_201_CREATED)



class ReviewSerializer(serializers.ModelSerializer):


    class Meta: 
        model = Review
        fields = ('id', 'waver_user', 'gear', 'review', 'created_on' )
        depth = 2
        