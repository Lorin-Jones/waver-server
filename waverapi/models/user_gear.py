from django.db import models

class UserGear(models.Model):

    user = models.ForeignKey('WaverUser', on_delete=models.CASCADE, related_name="gear_user")
    gear = models.ForeignKey('Gear', on_delete=models.CASCADE, related_name="user_gear")