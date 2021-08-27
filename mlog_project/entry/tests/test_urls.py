from django.test import TestCase
from django.urls import resolve

from entry import views
import entry.models
import musics.models
import accounts.models

class TestEntryUrls(TestCase):
	
	def setUp(self):

		test_genre = musics.models.Genre.objects.create(genre_name = 'test genre')

		self.test_artist = musics.models.Artist.objects.create(
			artist_name = 'test artist',
			slug = 'testartist',
		)
		self.test_artist.genre.add(test_genre)

		self.test_song = musics.models.Song.objects.create(song_name = 'test song')
		self.test_song.artist.add(self.test_artist)
		self.test_song.genre.add(test_genre)

		self.test_user_for_entry = accounts.models.User.objects.create(
			username = 'testuserforentry',
			handle = 'testuser for entry',
		)

		self.entry_instance = entry.models.Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = self.test_song,
			writer = self.test_user_for_entry
		)

	def test_create(self):
		view = resolve('/entry/create/')
		self.assertEqual(view.func.view_class, views.EntryCreateView)

	def test_detail(self):
		view = resolve('/entry/detail/%s/'%(self.entry_instance.pk))
		self.assertEqual(view.func.view_class, views.EntryDetailView)

	def test_update(self):
		view = resolve('/entry/update/%s/'%(self.entry_instance.pk))
		self.assertEqual(view.func.view_class, views.EntryUpdateView)

	def test_delete(self):
		view = resolve('/entry/delete/%s/'%(self.entry_instance.pk))
		self.assertEqual(view.func.view_class, views.EntryDeleteView)

	def test_entry_list_by_song(self):
		view = resolve('/entry/list/song/%s/'%(self.test_song.pk))
		self.assertEqual(view.func.view_class, views.EntryListBySongView)
	
	def test_entry_list_by_artist(self):
		view = resolve('/entry/list/artist/%s/'%(self.test_artist.slug))
		self.assertEqual(view.func.view_class, views.EntryListByArtistView)