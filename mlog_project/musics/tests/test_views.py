from django.http import response
from django.test import TestCase, RequestFactory
from django.urls import reverse

from utils import utils_for_test

from musics.models import Genre, Song
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
					'artist':artist,
					'genre':genre
					}
				)
			song = Song.objects.first()
			self.assertEqual(response.status_code, 302)
			self.assertRedirects(response, reverse('musics:song_detail', kwargs={'pk':song.id}))