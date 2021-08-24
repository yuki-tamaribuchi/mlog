from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve

from favorite_artists import views
import accounts.models
import musics.models

class TestFavoriteArtistsUrls(TestCase):
	@classmethod
	def setUp(cls):

		test_genre = musics.models.Genre.objects.create(genre_name = 'test genre')

		test_artist = musics.models.Artist.objects.create(
			artist_name = 'test artist',
			slug = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_user = accounts.models.User.objects.create(
			username = 'testuser',
			handle = 'testuser',
		)

	def test_process(self):
		view = resolve('/favorites/process/')
		self.assertEqual(view.func.view_class, views.FavoriteArtistProcess)

	def test_user_favorites_artist_list(self):
		artist_instance = musics.models.Artist.objects.first()
		slug = artist_instance.slug
		view = resolve('/favorites/artist/%s/'%(slug))
		self.assertEqual(view.func.view_class, views.UserFavoritesArtistListView)

	def test_user_favorites_artist_list(self):
		user_instance = accounts.models.User.objects.first()
		username = user_instance.username
		view = resolve('/favorites/user/%s/'%(username))
		self.assertEqual(view.func.view_class, views.UserFavoritesArtistListView)