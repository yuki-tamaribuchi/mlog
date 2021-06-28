from django.db import models

from accounts.models import User
from mlog.models import Entry, Artist, Song


class EntryReadActivity(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	entry=models.ForeignKey(Entry, on_delete=models.CASCADE)

	def __str__(self):
		return '%s read %s'%(self.user.username, self.entry.title)


class ArtistCheckedActivity(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return '%s checked %s'%(self.user.username, self.artist.artist_name)


class SongCheckedActivity(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	song=models.ForeignKey(Song, on_delete=models.CASCADE)

	def __str__(self):
		return '%s checked %s'%(self.user.username, self.song.song_name)


class UserDetailCheckedActivity(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='logined_user')
	detail_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='detail_user')

	def __str__(self):
		return '%s checked %s'%(self.user.username, self.detail_user.username)