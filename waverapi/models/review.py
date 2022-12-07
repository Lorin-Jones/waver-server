from django.db import models
from waverapi.models.waver_user import WaverUser

class Review(models.Model):

    user = models.ForeignKey(WaverUser, on_delete=models.CASCADE)
    gear = models.ForeignKey('Gear', on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=1000)
    created_on = models.DateField()