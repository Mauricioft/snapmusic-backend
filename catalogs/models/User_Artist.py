from django.db import models
from django.contrib.auth.models import User
from .Artist import Artist

class User_Artist(models.Model):
    user = models.ForeignKey(User, related_name='user_artist', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name='artist_artist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
