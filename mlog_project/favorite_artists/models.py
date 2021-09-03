from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from musics.models import Artist

class FavoriteArtist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name=_('artist'))

    def __str__(self):
        return '%s favorite artist is %s'%(self.user.username, self.artist.artist_name)