from activity import models
from mlog_project.celery import app

from accounts.models import User
from entry.models import Entry
from musics.models import Artist, Song

@app.task()
def entry_read_activity(pk, username):
	current_entry = Entry.objects.get(pk=pk)

	if username:
		current_user = User.objects.get(username=username)
		models.EntryReadActivity.objects.create(
			entry=current_entry,
			user=current_user
		)
	else:
		models.EntryReadActivity.objects.create(
			entry=current_entry
		)


@app.task()
def artist_checked_activity(aritst_name_id, username):
	if username:
		current_artist = Artist.objects.get(artist_name_id=aritst_name_id)
		current_user = User.objects.get(username=username)
		models.ArtistCheckedActivity.objects.create(
			artist=current_artist,
			user=current_user
		)


@app.task()
def song_checked_activity(song_pk, username):
	if username:
		current_song = Song.objects.get(pk=song_pk)
		current_user = User.objects.get(username=username)
		models.SongCheckedActivity.objects.create(
			song=current_song,
			user=current_user
		)