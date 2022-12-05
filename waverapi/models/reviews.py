from django.db import models

class Reviews(models.Model):

    user = models.ForeignKey()