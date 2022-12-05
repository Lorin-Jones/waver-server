from django.db import models

class Specifications(models.Model):

    description = models.CharField(max_length=100)