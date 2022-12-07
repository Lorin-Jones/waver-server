from django.db import models

class Specification(models.Model):

    description = models.CharField(max_length=100)