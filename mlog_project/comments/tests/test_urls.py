from django.test import TestCase
from django.urls import resolve

from comments import views
import entry.models
import musics.models
import accounts.models

class TestCommentsUrls(TestCase):

	@classmethod
	def setUp(cls):
		test_genre = musics.models.Genre.objects.create(genre_name = 'test genre')

		test_artist = musics.models.Artist.objects.create(
			artist_name = 'test artist',
			artist_name_id = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_song = musics.models.Song.objects.create(song_name = 'song name')
		test_song.artist.add(test_artist)
		test_song.genre.add(test_genre)

		test_user_for_entry = accounts.models.User.objects.create(
			username='testuserforentry',
			handle='testuser for entry',
		)

		test_entry = entry.models.Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = test_song,
			writer = test_user_for_entry
		)
	
	def test_create(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/comments/create/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.CommentCreateView)

	def test_list(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/comments/list/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.CommentListView)