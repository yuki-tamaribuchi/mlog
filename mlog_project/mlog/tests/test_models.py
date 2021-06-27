#https://qiita.com/tmasuyama/items/efbbc0f3af52d6a5dee4

from django.test import TestCase
from mlog.models import Artist, Genre

class GenreModelTests(TestCase):
	def test_is_empty(self):
		saved_genres=Genre.objects.all()
		self.assertEqual(saved_genres.count(),0)

	def test_is_count_one(self):
		genre=Genre(genre_name='test_genre')
		genre.save()
		saved_genres=Genre.objects.all()
		self.assertEqual(saved_genres.count(),1)

	def test_saving_and_retrieving_genre(self):
		genre=Genre()
		genre_name='test_genre_to_retrieve'
		genre.genre_name=genre_name
		genre.save()

		saved_genres=Genre.objects.all()
		actual_genre=saved_genres[0]

		self.assertEqual(actual_genre.genre_name, genre_name)


class ArtistModelTests(TestCase):

	def test_is_empty(self):
		saved_artists=Artist.objects.all()
		self.assertEqual(saved_artists.count(),0)

	def test_is_count_one(self):
		genre=Genre(genre_name='test_genre')
		genre.save()
		artist=Artist(artist_name='test_artist')
		artist.save()
		artist.genre.set([genre])

		saved_artists=Artist.objects.all()
		self.assertEqual(saved_artists.count(),1)

	def test_saving_and_retrieving_artist(self):
		genre=Genre()
		genre_name='test_genre_to_retrieve'
		genre.genre_name=genre_name
		genre.save()

		artist=Artist()
		artist_name='test_artist_to_retrieve'
		artist.artist_name=artist_name
		artist.save()
		artist.genre.set([genre])

		saved_artists=Artist.objects.all()
		actual_artist=saved_artists[0]


		self.assertEqual(actual_artist.artist_name,artist_name)
		self.assertEqual(actual_artist.genre.all()[0].genre_name,genre_name)


	def test_saving_and_retrieving_artist_with_two_genres(self):
		genres=[Genre() for _ in range(2)]
		genre_names=['test_genre_to_retrieve1', 'test_genre_to_retrieve2']
		
		for i,genre_name in enumerate(genre_names):
			genres[i].genre_name=genre_name
			genres[i].save()

		artist=Artist()
		artist_name='test_artist_to_retrieve_with_two_genres'
		artist.artist_name=artist_name
		artist.save()
		artist.genre.set(genres)

		saved_artists=Artist.objects.all()
		actual_artist=saved_artists[0]

		self.assertEqual(actual_artist.artist_name,artist_name)
		self.assertEqual(actual_artist.genre.all()[0].genre_name,genre_names[0])
		self.assertEqual(actual_artist.genre.all()[1].genre_name,genre_names[1])
