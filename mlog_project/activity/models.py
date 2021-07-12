from django.db import models

from accounts.models import User
from entry.models import Entry
from musics.models import Artist, Song, Genre


class EntryReadActivity(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
	entry = models.ForeignKey(Entry, on_delete = models.CASCADE)

	def __str__(self):
		if self.user:
			return '%s read %s'%(self.user.username, self.entry.title)
		else:
			return 'Unknown user read %s'%(self.entry.title)


class ArtistCheckedActivity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)

    def __str__(self):
        return '%s checked %s'%(self.user.username, self.artist.artist_name)


class SongCheckedActivity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	song = models.ForeignKey(Song, on_delete=models.CASCADE)

	def __str__(self):
		return '%s checked %s'%(self.user.username, self.song.song_name)


class UserDetailCheckedActivity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logined_user')
	detail_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='detail_user')

	def __str__(self):
		return '%s checked %s'%(self.user.username, self.detail_user.username)


class GenreCheckedActivity(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete = models.CASCADE)

	def __str__(self):
		return '%s checked %s'%(self.user, self.genre)