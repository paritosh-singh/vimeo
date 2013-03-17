from django.db import models

# User model for storing user data
class User(models.Model):
    vimeo_id = models.IntegerField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    paying = models.BooleanField(default=False)
    staffpick = models.BooleanField(default=False)
    uploaded = models.BooleanField(default=False)