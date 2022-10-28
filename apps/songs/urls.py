from django.urls import path
from . import views

app_name="songs_"
urlpatterns = [
    path('collections', views.selectAllSongAlbumPhotos, name="selectAllSongAlbumPhotos"),
    path('songs', views.selectAllSong, name="selectAllSong"),
    path('sorting-results', views.selectedSortedSearch, name="selectedSortedSearch"),
]



