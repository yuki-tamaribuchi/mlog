from django.test import TestCase
from django.urls import resolve

from musics import views
import musics.models

class TestMusicsUrls(TestCase):
	@classmethod
	def setUp(cls):
		test_genre = musics.models.Genre.objects.create(genre_name = 'test genre')

		test_artist = musics.models.Artist.objects.create(
			artist_name = 'test artist',
			artist_name_id = 'testartist',
			artist_biograph = 'test biograph'
		)
		test_artist.genre.add(test_genre)

		test_song = musics.models.Song.objects.create(
			song_name = 'test song',
		)
		test_song.genre.add(test_genre)
		test_song.artist.add(test_artist)

	def test_artist_detail(self):
		artist_instance = musics.models.Artist.objects.first()
		artist_name_id = artist_instance.artist_name_id
		view = resolve('/musics/detail/artist/%s/'%(artist_name_id))
		self.assertEqual(view.func.view_class, views.ArtistDetailView)

	def test_song_detail(self):
		song_instance = musics.models.Song.objects.first()
		pk = song_instance.pk
		view = resolve('/musics/detail/song/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.SongDetailView)

	def test_song_create(self):
		view = resolve('/musics/create/song/')
		self.assertEqual(view.func.view_class, views.SongCreateView)

	def test_create_artist(self):
		view = resolve('/musics/create/artist/')
		self.assertEqual(view.func.view_class, views.ArtistCreateView)

	def test_create_genre(self):
		view = resolve('/musics/create/genre/')
		self.assertEqual(view.func.view_class, views.GenreCreateView)

	def test_create_song_popup(self):
		view = resolve('/musics/create/song/popup/')
		self.assertEqual(view.func.view_class, views.PopupSongCreateView)
	
	def test_create_artist_popup(self):
		view = resolve('/musics/create/artist/popup/')
		self.assertEqual(view.func.view_class, views.PopupArtistCreateView)

	def test_create_genre_popup(self):
		view = resolve('/musics/create/genre/popup/')
		self.assertEqual(view.func.view_class, views.PopupGenreCreateView)

	def test_genre_list(self):
		view = resolve('/musics/list/genre/')
		self.assertEqual(view.func.view_class, views.GenreListView)

	def test_list(self):
		genre_instance = musics.models.Genre.objects.first()
		genre_name = genre_instance.genre_name
		view = resolve('/musics/list/genre/%s/artist/'%(genre_name))
		self.assertEqual(view.func.view_class, views.ArtistByGenreListView)