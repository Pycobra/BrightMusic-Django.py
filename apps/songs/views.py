from django.http import JsonResponse, HttpResponse

from ..core.views import fetchAllModel, getArtist

def selectAllSongAlbumPhotos(request):
    if request.GET:
        arrayObj = getArtist()
        response = JsonResponse({'albumPhotoCheckedState': arrayObj})
        return response
    return HttpResponse()
        
def selectAllSong(request):
    return selectAllSongAlbumPhotos(request)
    
def selectedSortedSearch(request):
    if request.GET:
        value = request.GET.get('value')
        songs = fetchAllModel('songs')
        artistImg = fetchAllModel('artist-image')
        if value == 'Genre':
            songsOrdered = songs.order_by('genre')
        elif value == 'Artist':
            songsOrdered = songs.order_by('artist__name')
        elif value == 'Release Year':
            songsOrdered = songs.order_by('release_year')
        elif value == 'Label':
            songsOrdered = songs.order_by('label')
        groupedList = []
        def uniqueAppender(model):
            print( model.artist.name, model.genre)
            if value == 'Genre':
                sortOption = model.genre
            elif value == 'Artist':
                sortOption = model.artist.name
            elif value == 'Release Year':
                sortOption = model.release_year.year
            elif value == 'Label':
                sortOption = model.label
            if len(groupedList) > 0:
                for i in groupedList:
                    for key in i.keys():
                        if str(sortOption) == str(key):
                            # print(model.genre, model.artist.name, model.title, "PART-2")
                            # i[f'{key}'].append({'name':  model.artist.name, 'title': model.title, 'id':  model.id, 
                            #     'selected': False, 'url': model.artist.artist_images.all()[0].images.url, #list(map(lambda i: i.images.url, model.artist.artist_images.all()[0])), 
                            #     'songs': songs.filter(artist__id = model.artist.id).count()})
                            i[f'{key}'].append({'url': model.images.url, 'name': model.artist.name, 'title':model.title, 
                                'release_year': model.release_year.year, 'label': model.label, 
                                'genre': model.genre, 'id': model.id, 'selected': False,
                                'minutes': model.minutes, 'format': model.format})
                            position=groupedList.index(i)
                            groupedList.remove(i)
                            groupedList.insert(position, i)
                            return i
            groupedList.append({f'{sortOption}': [{'url': model.images.url, 'name': model.artist.name, 'title':model.title, 
                                'release_year': model.release_year.year, 'label': model.label, 
                                'genre': model.genre, 'id': model.id, 'selected': False,
                                'minutes': model.minutes, 'format': model.format}]})
            # groupedList.append({f'{sortOption}': [{'name':  model.artist.name, 'id':  model.artist.id, 
            #         'selected': False, 'url': model.artist.artist_images.all()[0].images.url, 
            #         'songs':   songs.filter(artist__id = model.artist.id).count()}]})
        list(map(lambda model: uniqueAppender(model), songsOrdered))
        # print(groupedList)
        response = JsonResponse({'albumPhotoCheckedState': groupedList})
        return response
    return HttpResponse()
