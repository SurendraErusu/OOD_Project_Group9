from django.db import models
from Login.models import CustomUser
from posts.models import Post

class SearchUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Add other fields as needed

class SearchPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Add other fields as needed

