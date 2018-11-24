from django.db import models
from .Gender import Gender

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=80)
    gender_id = models.ForeignKey(Gender, related_name='artist', on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    music_genre = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def gender(self):
        return self.gender_id