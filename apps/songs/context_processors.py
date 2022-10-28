from ..core.views import getArtist

def selectAllSongAlbumPhotos(request):
    return {'albumPhotoCheckedState': getArtist(), 'currentPage': 'FIRST-PAGE'}


