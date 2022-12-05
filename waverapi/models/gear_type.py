from django.db import models

class GearType(models.Model):

    name = models.CharField(max_length=50)