# import serializers
from .serializers import ArtistSerializer
from .serializers import GenderSerializer
from .serializers import AlbumSerializer

# import library rest_framework
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import (
    api_view,
    renderer_classes,
    permission_classes,
    authentication_classes
)
from rest_framework.parsers import JSONParser
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

# import models
from .models import Artist
from .models import Gender
from .models import Album

# import models
from datetime import datetime

# Create your views here.
@api_view(['GET','PUT','POST', 'DELETE'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny, ))
def ArtistList(request, format=None):

    reponse = {
        'success': False,
        'result': [],
        'error': {
            'code': '',
            'msg': ''
        },
        'message': {
            'msg': '',
            'type': ''
        }
    }

    if request.method == 'GET':
        try:
            status_http = status.HTTP_201_CREATED
            if  not request.GET:
                artists = Artist.objects.all()
                serializer = ArtistSerializer(artists, many=True)  # serialize the data

                reponse['result'] = serializer.data
                reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)

    if request.method == 'POST':
        try:
            status_http = status.HTTP_201_CREATED
            serializer = ArtistSerializer(data=request.data)
            if serializer.is_valid():
                valid_data = serializer.data
                artist = Artist.objects.filter(name=valid_data.get('name'))
                if artist.exists():
                    reponse['result'] = False
                    reponse['message']['type'] = 'warning'
                    reponse['message']['msg'] = "Este artista ya se ha registrado"
                else:
                    serializer.create(valid_data)
                    reponse['result'] = True
                    reponse['message']['type'] = 'success'
                    reponse['message']['msg'] = 'Su artista fue creado'
            else:
                reponse['result'] = False
                reponse['message']['type'] = 'warning'
                reponse['message']['msg'] = serializer.errors

            reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)

# Create your views here.
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny, ))
def GenderList(request, format=None):

    reponse = {
        'success': False,
        'result': [],
        'error': {
            'code': '',
            'msg': ''
        },
        'message': {
            'msg': '',
            'type': ''
        }
    }

    if request.method == 'GET':
        try:
            status_http = status.HTTP_201_CREATED
            if  not request.GET:
                gender = Gender.objects.all()
                serializer = GenderSerializer(gender, many=True)  # serialize the data

                reponse['result'] = serializer.data
                reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)


# Create your views here.
@api_view(['GET','PUT','DELETE'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny, ))
def ArtistDetail(request, pk):

    reponse = {
        'success': False,
        'result': [],
        'error': {
            'code': '',
            'msg': ''
        },
        'message': {
            'msg': '',
            'type': ''
        }
    }

    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        reponse['message']['type'] = 'warning'
        reponse['message']['msg'] = 'El artista no existe'
        return Response(reponse, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            status_http = status.HTTP_201_CREATED

            serializer = ArtistSerializer(artist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                reponse['result'] = True
                reponse['message']['type'] = 'success'
                reponse['message']['msg'] = 'El artista fue editado'
            else:
                reponse['result'] = False
                reponse['message']['type'] = 'warning'
                reponse['message']['msg'] = serializer.errors

            reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)

    if request.method == 'DELETE':
        try:
            status_http = status.HTTP_201_CREATED
            artist.delete()
            reponse['result'] = True
            reponse['message']['type'] = 'success'
            reponse['message']['msg'] = 'El artista fue eliminado'

            reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)

# Create your views here.
@api_view(['GET','PUT','POST', 'DELETE'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny, ))
def AlbumList(request, format=None):

    reponse = {
        'success': False,
        'result': [],
        'error': {
            'code': '',
            'msg': ''
        },
        'message': {
            'msg': '',
            'type': ''
        }
    }

    if request.method == 'GET':
        try:
            status_http = status.HTTP_201_CREATED
            if  not request.GET:
                album = Album.objects.all()
                serializer = AlbumSerializer(album, many=True)  # serialize the data

                reponse['result'] = serializer.data
                reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)

    if request.method == 'POST':
        try:
            status_http = status.HTTP_201_CREATED
            serializer = ArtistSerializer(data=request.data)
            if serializer.is_valid():
                valid_data = serializer.data
                artist = Artist.objects.filter(name=valid_data.get('name'))
                if artist.exists():
                    reponse['result'] = False
                    reponse['message']['type'] = 'warning'
                    reponse['message']['msg'] = "Este artista ya se ha registrado"
                else:
                    serializer.create(valid_data)
                    reponse['result'] = True
                    reponse['message']['type'] = 'success'
                    reponse['message']['msg'] = 'Su artista fue creado'
            else:
                reponse['result'] = False
                reponse['message']['type'] = 'warning'
                reponse['message']['msg'] = serializer.errors

            reponse['success'] = True
        except ValueError as e:
            status_http = status.HTTP_400_BAD_REQUEST
            reponse['error']['code'] = status_http
            reponse['error']['msg'] = e.args

        return Response(reponse, status=status_http)
