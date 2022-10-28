import uuid
import secrets

from django.db import models
from django.core.files import File
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name

# class Song(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     artist = models.ForeignKey(Artist, related_name="artist_songs", verbose_name=_("Artist"), on_delete=models.CASCADE)
#     images = models.ImageField(verbose_name=_("image"),
#                                help_text=_("Upload song image"),
#                                upload_to="images/uploads/", default="images/others/igor-lypnytskyi-PobecUzsK4c-unsplash.png")
#     release_year = models.DateField()
#     title = models.CharField(_("Title"), max_length=50)
#     label = models.CharField(_("Label"), max_length=50)
#     format = models.CharField(_("Format"), max_length=50)
#     minutes = models.CharField(_("Minutes"), max_length=50)
#     genre = models.CharField(_("Genre"), max_length=50)
#     created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

#     class Meta:
#         verbose_name = "Song"
#         verbose_name_plural = "Songs"

#     def __str__(self):
#         return "Song"

class ArtistImages(models.Model):
    artist = models.ForeignKey(Artist, related_name="artist_images", verbose_name=_("Artist"), on_delete=models.CASCADE)
    images = models.ImageField(verbose_name=_("image"),
                               help_text=_("Upload a artist image"),
                               upload_to="images/uploads/", default="images/others/igor-lypnytskyi-PobecUzsK4c-unsplash.png")
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name =_("Artist Image")
        verbose_name_plural = _("Artist Images")

    
    def __str__(self):
        return self.artist.name