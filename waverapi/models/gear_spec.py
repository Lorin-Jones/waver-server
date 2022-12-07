from django.db import models

class GearSpec(models.Model):

    gear = models.ForeignKey('Gear', on_delete=models.CASCADE)
    specifications = models.ForeignKey('Specification', on_delete=models.CASCADE)