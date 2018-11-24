from django.contrib.auth.models import User
from rest_framework.serializers import (
    CharField,
    IntegerField,
    ModelSerializer,
    ValidationError,
    Field,
    HyperlinkedModelSerializer
)
from .models.Artist import Artist
from .models.Gender import Gender
from .models.User_Artist import User_Artist

class GenderSerializer(ModelSerializer):
    name = CharField(required=True, max_length=80)

    class Meta:
        model = Gender
        fields = ('id', 'name')

class ArtistSerializer(ModelSerializer):
    name = CharField(required=True, max_length=80)
    gender = GenderSerializer(read_only=True)
    age = IntegerField(required=True)
    city = CharField(required=True, max_length=100)
    country = CharField(required=True, max_length=100)
    nationality = CharField(required=True, max_length=100)
    music_genre = CharField(required=True, max_length=250)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'gender_id', 'age', 'city', 'country', 'nationality', 'music_genre', 'gender')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        name = validated_data['name']
        gender_id = validated_data['gender_id']
        age = validated_data['age']
        city = validated_data['city']
        country = validated_data['country']
        nationality = validated_data['nationality']
        music_genre = validated_data['music_genre']

        artist = Artist(
            name=name,
            gender_id_id=gender_id,
            age=age,
            city=city,
            country=country,
            nationality=nationality,
            music_genre=music_genre
        )

        artist.save()

        return validated_data

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'music_genre', 'release_date', 'album_name', 'record_label', 'songs', 'formats', 'qualification', 'avatar', 'language', 'classification', 'artist_id_id')

