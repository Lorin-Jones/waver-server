from django.db import models

class UsedGear(models.Model):

    waver_user = models.ForeignKey("WaverUser", on_delete=models.CASCADE)
    item = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    price = models.IntegerField()
    details = models.CharField(max_length=1000)