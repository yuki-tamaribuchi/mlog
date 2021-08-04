from django.test import TestCase
from django.urls import resolve

from entry import views
import entry.models
import musics.models
import accounts.models

class TestEntryUrls(TestCase):
	@classmethod
	def setUp(cls):

		test_genre = musics.models.Genre.objects.create(genre_name = 'test genre')

		test_artist = musics.models.Artist.objects.create(
			artist_name = 'test artist',
			slug = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_song = musics.models.Song.objects.create(song_name = 'test song')
		test_song.artist.add(test_artist)
		test_song.genre.add(test_genre)

		test_user_for_entry = accounts.models.User.objects.create(
			username = 'testuserforentry',
			handle = 'testuser for entry',
		)

		entry.models.Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = test_song,
			writer = test_user_for_entry
		)

	def test_create(self):
		view = resolve('/entry/create/')
		self.assertEqual(view.func.view_class, views.EntryCreateView)

	def test_detail(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/entry/detail/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.EntryDetailView)

	def test_update(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/entry/update/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.EntryUpdateView)

	def test_delete(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/entry/delete/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.EntryDeleteView)