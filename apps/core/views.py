
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from ..artists.models import Artist, ArtistImages
from ..songs.models import Song


def fetchAllModel(model):
    if model == 'songs':
        return Song.objects.all()
    if model == 'artist':
        return Artist.objects.all()
    if model == 'artist-image':
        return ArtistImages.objects.all()

def getArtist():
    songs = fetchAllModel('songs')
    arrayObj = list()
    mapped = list(map(lambda x: {
            'url': x.images.url, 'name': x.artist.name, 'title':x.title, 
            'release_year': x.release_year.year, 'label': x.label, 
            'genre': x.genre, 'id': x.id, 'selected': False,
            'minutes': x.minutes, 'format': x.format
            }, songs))
    return mapped

def frontpage(request):
    arrayObj = getArtist()
    return render(request, 'core/landingpage/landingpage.html', {'collections': arrayObj})
            
