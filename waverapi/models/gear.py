from django.db import models

class Gear(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    release_date = models.IntegerField()
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE, related_name='manufacturer')
    gear_type = models.ForeignKey('GearType', on_delete=models.CASCADE)