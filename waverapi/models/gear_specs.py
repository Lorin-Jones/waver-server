from django.db import models

class GearSpecs(models.Model):

    gear = models.ForeignKey('Gear', on_delete=models.CASCADE)
    specifications = models.ForeignKey('Specifications', on_delete=models.CASCADE)