from django.conf.urls import url
from catalogs import views

urlpatterns = [
    url(r'^artist/$', views.ArtistList),
    url(r'^artist/(?P<pk>[0-9]+)$', views.ArtistDetail),
    url(r'^album/$', views.AlbumList),
	url(r'^combos/gender/$', views.GenderList),
]
