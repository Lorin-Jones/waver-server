from django.db import models

class Gear(models.Model):

    image = models.CharField()
    price = models.IntegerField()
    description = models.CharField()
    specifications = models.ManyToManyField("Specifications", through='GearSpecs')
    release_date = models.IntegerField()
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE, related_name='manufacturer')
    gear_type = models.ForeignKey('Gear', on_delete=models.CASCADE, related_name='gear_type')