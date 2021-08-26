from django.test import TestCase
from django.urls import resolve

from likes import views
import likes.models
import musics.models
import accounts.models
import entry.models

class TestLikeUrls(TestCase):
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

		test_entry = entry.models.Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = test_song,
			writer = test_user_for_entry
		)

		test_user_for_like = accounts.models.User.objects.create(
			username = 'testuserforlike',
			handle = 'testuser for like',
		)

		likes.models.Like.objects.create(
			user = test_user_for_like,
			entry = test_entry
		)

	'''
	def test_process(self):
		view = resolve('/likes/process/')
		self.assertEqual(view.func.view_class, views.LikeProcess)
	'''

	def test_like(self):
		view = resolve('/likes/like/')
		self.assertEqual(view.func, views.like_process)

	def test_user_like_list(self):
		view = resolve('/likes/userlist/testuserforlike/')
		self.assertEqual(view.func.view_class, views.UsersLikeListView)

	def test_entry_like_list(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/likes/entrylist/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.EntrysLikeListView)