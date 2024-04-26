from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')
    document = models.ForeignKey('Document', on_delete=models.CASCADE, null=True, blank=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.TextField()
    document = models.ForeignKey('Document', on_delete=models.CASCADE, null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    blame = models.IntegerField(default=0)
    access_level = models.IntegerField()
    access_teams = models.CharField(max_length=100)  # Assuming teams are stored as a comma-separated string
    blames = models.JSONField(default=list)
    datetime_posted = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    pdf_file = models.FileField(upload_to='documents/')

