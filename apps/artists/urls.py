from django.urls import path
from . import views

app_name="artist_"
urlpatterns = [
    path('artists', views.profileAllArtists, name="profileAllArtists"),
    path('artists-profile', views.selectProfileOfSingleArtists, name="selectProfileOfSingleArtists"),
]



