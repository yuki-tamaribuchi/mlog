from django.test import TestCase

from favorite_artists.models import FavoriteArtist
from accounts.models import User
from musics.models import Artist, Genre


class TestFavoriteArtist(TestCase):

	@classmethod
	def setUp(cls):
		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_artist = Artist.objects.create(
			artist_name = 'test artist',
			slug = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_user = User.objects.create(
			username = 'test user',
			handle = 'testuser',
		)

		FavoriteArtist.objects.create(
			user = test_user,
			artist = test_artist
		)

	def test_str(self):
		fav=FavoriteArtist.objects.all().first()
		self.assertEqual(str(fav), 'test user favorite artist is test artist')