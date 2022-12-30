from django.db import models
from waverapi.models.waver_user import WaverUser

class Post(models.Model):
    user = models.ForeignKey(WaverUser, on_delete=models.CASCADE, related_name='posts')
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    content = models.TextField()