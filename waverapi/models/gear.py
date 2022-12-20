from django.db import models

class Gear(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    specifications = models.ForeignKey('Specification', on_delete=models.CASCADE)
    reviews = models.ManyToManyField('Review', through='GearReview')
