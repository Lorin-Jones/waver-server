from django.db import models
from waverapi.models.waver_user import WaverUser

class Review(models.Model):

    waver_user = models.ForeignKey(WaverUser, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    rating = models.IntegerField()
    created_on = models.DateField()