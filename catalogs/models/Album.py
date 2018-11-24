from django.db import models
from .Artist import Artist

# Create your models here.
class Album(models.Model):
    artist_id = models.ForeignKey(Artist, related_name='album', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    music_genre = models.CharField(max_length=250)
    release_date= models.DateField()
    album_name = models.CharField(max_length=100)
    record_label = models.CharField(max_length=100)
    songs = models.IntegerField()
    formats = models.CharField(max_length=100)
    qualification = models.IntegerField()
    avatar = models.CharField(max_length=250)
    language = models.CharField(max_length=40)
    classification = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)