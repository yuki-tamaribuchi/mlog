from django.test import TestCase
from django.urls import reverse

from entry.views import EntryDetailView


def create__test_genre():
	from musics.models import Genre
	genre_instance = Genre.objects.create('test genre')
	return genre_instance

def create__test_artist():
	from musics.models import Artist
	aritst_instance = Artist.objects.create(
		artist_name = 'test artist',
		artist_name_id = 'testartist'
	)
	aritst_instance.genre.add(create_test_genre())
	return aritst_instance

def create_test_song():
	from musics.models import Song
	song_instance = Song.objects.create(
		song_name = 'test song'
	)
	song_instance.artist.add(create_test_artist()),
	song_instance.genre.add(create_test_genre()),

def create_test_user():
	from accounts.models import User
	user_instance = User.objects.create(
		username = 'testuser',
		handle = 'test handle',
		biograph = 'test biograph'
	)


def create_test_entry():
	from entry.models import Entry
	entry_instance = Entry.objcets.create(
		title = 'test entry',
		content = 'test content',
		writer = create_test_user(),
		song = create_test_song()
	)


class EntryDetailViewTest(TestCase):

	def test_no_entry(self):
		response = self.client.get(reverse('entry:detail',args = (1,)))
		self.assertEqual(response.status_code, 404)