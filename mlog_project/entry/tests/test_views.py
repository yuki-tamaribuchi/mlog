'''
from django.test import TestCase
from django.urls import reverse

from entry.views import EntryDetailView


def create_test_genre():
	from musics.models import Genre
	genre_instance = Genre.objects.create(genre_name = 'test genre')
	return genre_instance

def create_test_artist():
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
	song_instance.artist.add(create_test_artist())
	song_instance.genre.add(create_test_genre())
	return song_instance

def create_test_user():
	from accounts.models import User
	user_instance = User.objects.create(
		username = 'testuser',
		handle = 'test handle',
		biograph = 'test biograph'
	)
	return user_instance


def create_test_entry():
	from entry.models import Entry
	entry_instance = Entry.objects.create(
		title = 'test entry',
		content = 'test content',
		writer = create_test_user(),
		song = create_test_song()
	)
	return entry_instance


class EntryDetailViewTest(TestCase):

	@classmethod
	def setUp(cls):
		create_test_entry()

	def test_not_exist_entry(self):
		response = self.client.get(reverse('entry:detail',args = (2,)))
		self.assertEqual(response.status_code, 404)
'''