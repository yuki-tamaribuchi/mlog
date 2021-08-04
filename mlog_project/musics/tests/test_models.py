from django.test import TestCase
from django.test.utils import get_runner

from musics.models import Genre, Artist, Song


class TestGenre(TestCase):

	@classmethod
	def setUp(cls):
		Genre.objects.create(genre_name = 'test genre')
	
	def test_genre_name_max_length(self):
		genre_instance = Genre.objects.all().first()
		max_length = genre_instance._meta.get_field('genre_name').max_length
		self.assertEqual(max_length, 20)

	def test_str(self):
		genre_instance = Genre.objects.all().first()
		self.assertEqual(str(genre_instance), 'test genre')


class TestArtist(TestCase):

	@classmethod
	def setUp(cls):

		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_artist = Artist.objects.create(
			artist_name = 'test artist',
			slug = 'testartist',
			artist_biograph = 'test biograph'
		)
		test_artist.genre.add(test_genre)

	def test_artist_name_max_length(self):
		artist_instance = Artist.objects.all().first()
		max_length = artist_instance._meta.get_field('artist_name').max_length
		self.assertEqual(max_length, 30)

	def test_slug_max_length(self):
		artist_instance = Artist.objects.all().first()
		max_length = artist_instance._meta.get_field('slug').max_length
		self.assertEqual(max_length, 30)

	def test_artist_biograph_max_length(self):
		artist_instance = Artist.objects.all().first()
		max_length = artist_instance._meta.get_field('artist_biograph').max_length
		self.assertEqual(max_length, 200)

	def test_str(self):
		artist_instance = Artist.objects.all().first()
		self.assertEqual(str(artist_instance), 'test artist')


class TestSong(TestCase):

	@classmethod
	def setUp(cls):
		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_artist = Artist.objects.create(
			artist_name = 'test artist',
			slug = 'testartist',
			artist_biograph = 'test biograph'
		)
		test_artist.genre.add(test_genre)

		test_song = Song.objects.create(
			song_name = 'test song',
		)
		test_song.genre.add(test_genre)
		test_song.artist.add(test_artist)

	def test_song_name_max_length(self):
		song_instance = Song.objects.all().first()
		max_length = song_instance._meta.get_field('song_name').max_length
		self.assertEqual(max_length, 30)

	def test_str(self):
		song_instance = Song.objects.all().first()
		self.assertEqual(str(song_instance), 'test song by test artist')