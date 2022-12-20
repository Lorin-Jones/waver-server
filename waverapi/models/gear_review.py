from django.db import models

class GearReview(models.Model):

    gear = models.ForeignKey('Gear', on_delete=models.CASCADE)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)