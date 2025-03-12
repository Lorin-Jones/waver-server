from django.db import models

class Specifications(models.Model):

    release_date = models.IntegerField()
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    gear_types = models.ForeignKey('GearType', on_delete=models.CASCADE)
    number_of_keys = models.CharField(max_length=50, null=True, blank=True)
    voices = models.CharField(max_length=50, null=True, blank=True)
    arpeggiator = models.BooleanField(null=True, default=None, blank=True)
    sequencer = models.BooleanField(null=True, default=None, blank=True)
    velocity = models.BooleanField(null=True, default=None, blank=True)
    aftertouch = models.BooleanField(null=True, default=None, blank=True)
