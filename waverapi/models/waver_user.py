from django.db import models
from django.contrib.auth.models import User

class WaverUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    bio = models.CharField(max_length=50)
    gear = models.ManyToManyField('Gear', through="UserGear")
    image = models.CharField(max_length=255, null=True, default=None, blank=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
