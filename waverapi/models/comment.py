from django.db import models
from .post import Post
from waverapi.models.waver_user import WaverUser

class Comment(models.Model):
    author = models.ForeignKey(WaverUser, on_delete=models.CASCADE, related_name="user_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    content = models.TextField()
