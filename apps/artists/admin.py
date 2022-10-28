from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import Artist, ArtistImages
from apps.songs.models import Song

class SongInline(admin.TabularInline):
    model = Song
    extra = 3
class ArtistImagesInline(admin.TabularInline):
    model = ArtistImages
    extra = 3
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [SongInline, ArtistImagesInline]
