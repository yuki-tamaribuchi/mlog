from django.http import response
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.urls.resolvers import get_resolver

from utils import utils_for_test

from musics.models import Genre, Song, Artist
from musics.views import ArtistDetailView


class ArtistDetailViewTest(TestCase):

	def setUp(self):
		self.artist = utils_for_test.create_test_artist(
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

	def test_template(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.artist.slug}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('musics/artist_detail.html')

	def test_entries_in_context(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.artist.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('entries', context)

	def test_members_in_context(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.artist.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('members', context)
	
	def test_song_list_in_context(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.artist.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('song_list', context)

	def test_fav_status_in_context_not_loggedin(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.artist.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertNotIn('fav_status', context)

	def test_fav_status_in_context_loggedin(self):
		user = utils_for_test.create_test_user(
			username='testuser',
			handle='test user',
			biograph='test biograph'
		)
		factory = RequestFactory()
		request = factory.get(reverse('musics:artist_detail', kwargs={'slug':self.artist.slug}))
		request.user = user
		response = ArtistDetailView.as_view()(request, slug=self.artist.slug)
		context = response.context_data
		self.assertEqual(response.status_code, 200)
		self.assertIn('fav_status', context)

	
class SongCreateViewTest(TestCase):

	def test_template(self):
		response = self.client.get(reverse('musics:song_create'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('musics/song_form.html')

	def test_success_url(self):
		artist = utils_for_test.create_test_artist(
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)
		genre = Genre.objects.first()
		response = self.client.post(
			path=reverse('musics:song_create'),
			data={
				'song_name':'test song',
				'artist':artist.id,
				'genre':genre.id
				}
			)
		song = Song.objects.first()
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('musics:song_detail', kwargs={'pk':song.id}))


class ArtistCreateViewTest(TestCase):
	def test_template(self):
		response = self.client.get(reverse('musics:artist_create'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/artist_form.html')

	def test_success_url(self):
		genre = utils_for_test.create_test_genre('test genre')
		response = self.client.post(
			path=reverse('musics:artist_create'),
			data={
				'artist_name':'test aritst',
				'slug':'testartist',
				'genre':genre.id
			}
		)
		artist = Artist.objects.first()
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('musics:artist_detail', kwargs={'slug':artist.slug}))


class SongDetailViewTest(TestCase):
	def setUp(self):
		self.song = utils_for_test.create_test_song(
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

	def test_template(self):
		response = self.client.get(reverse('musics:song_detail', kwargs={'pk':self.song.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/song_detail.html')

	def test_entries_in_context(self):
		response = self.client.get(reverse('musics:song_detail', kwargs={'pk':self.song.id}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('entries', context)


class GenreCreateViewTest(TestCase):
	def test_template(self):
		response = self.client.get(reverse('musics:genre_create'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/genre_form.html')

	'''
	def test_success_url(self):
		response = self.client.post(
			path=reverse('musics:genre_create'),
			data={
				'genre_name':'test genre'
			}
		)
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('entry:create'))
	'''

class SongUpdateViewTest(TestCase):
	def setUp(self):
		self.song = utils_for_test.create_test_song(
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)
	
	def test_template(self):
		response = self.client.get(reverse('musics:song_update', kwargs={'pk':self.song.pk}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/song_form.html')


class GenreListViewTest(TestCase):
	def setUp(self):
		utils_for_test.create_test_genre(
			genre_name='test genre'
		)

	def test_template(self):
		response = self.client.get(reverse('musics:genre_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/genre_list.html')
	
	def test_queryset(self):
		values = Genre.objects.all()
		response = self.client.get(reverse('musics:genre_list'))
		self.assertQuerysetEqual(qs=response.context['genre_list'], values=values)


class ArtistByGenreListViewTest(TestCase):
	def setUp(self):
		self.artist = utils_for_test.create_test_artist(
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)
		self.genre = self.artist.genre.all()
	
	def test_template(self):
		response = self.client.get(reverse('musics:artist_by_genre', kwargs={'genre_name':self.genre[0].genre_name}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/artist_by_genre_list.html')

	def test_queryset(self):
		values = Artist.objects.filter(genre__genre_name=self.genre[0].genre_name)
		response = self.client.get(reverse('musics:artist_by_genre', kwargs={'genre_name':self.genre[0].genre_name}))
		self.assertQuerysetEqual(response.context['artist_list'], values=values)

	def test_genre_in_context(self):
		response = self.client.get(reverse('musics:artist_by_genre', kwargs={'genre_name':self.genre[0].genre_name}))
		self.assertIn('genre', response.context)


class SongByArtistListViewTest(TestCase):
	def setUp(self):
		self.song = utils_for_test.create_test_song(
			song_name='test song',
			artist_name='test artist',
			slug='test genre',
			genre_name='test genre'
		)
		self.artist = self.song.artist.all()
	
	def test_template(self):
		response = self.client.get(reverse('musics:song_by_artist', kwargs={'slug':self.artist[0].slug}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/song_by_artist_list.html')

	def test_queryset(self):
		values = Song.objects.filter(artist__slug=self.artist[0].slug)
		response = self.client.get(reverse('musics:song_by_artist', kwargs={'slug':self.artist[0].slug}))
		self.assertQuerysetEqual(response.context['song_list'], values=values)

	def test_artist_in_context(self):
		response = self.client.get(reverse('musics:song_by_artist', kwargs={'slug':self.artist[0].slug}))
		self.assertIn('artist', response.context)


class SearchSpotifyTracksTest(TestCase):
	def test_search(self):
		data = {
			'search_keywords':'the chainsmokers'
		}
		response = self.client.post(reverse('musics:search_spotify_tracks'), data)
		self.assertEqual(response.status_code, 200)


class SelectSpotifyTracksTest(TestCase):
	def test_get(self):
		response = self.client.get(reverse('musics:select_spotify_tracks'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'musics/spotify_track_select.html')

	'''
	def test_select(self):
		import json
		data = json.dumps({
			'selected_track':{
				'spotify_link':'https://open.spotify.com/track/6RUKPb4LETWmmr3iAEQktW',
				'preview_url':'https://p.scdn.co/mp3-preview/cb1ae1f9e2f874dd2d19e4c29edb552777eb1e7a?cid=95dbbb0b05f0404a82b397e6f20ef953',
				'artwork_url':'https://i.scdn.co/image/ab67616d0000b2730c13d3d5a503c84fcc60ae94'
			}
		})
		response = self.client.post(reverse('musics:select_spotify_tracks'), content_type='application/json', data=data)
	'''