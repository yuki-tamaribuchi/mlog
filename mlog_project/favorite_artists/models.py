from django.db import models

from accounts.models import User
from musics.models import Artist

class FavoriteArtist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return '%s favorite artist is %s'%(self.user.username, self.artist.artist_name)