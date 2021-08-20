from django.test import TestCase
from django.urls import reverse

from utils import utils_for_test


class ArtistDetailViewTest(TestCase):

	def setUp(self):
		self.entry = utils_for_test.create_test_artist(
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

	def test_template(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.entry.slug}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('musics/artist_detail.html')

	def test_entries_in_context(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.entry.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('entries', context)

	def test_members_in_context(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.entry.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('members', context)
	
	def test_song_list_in_context(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.entry.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertIn('song_list', context)

	def test_fav_status_in_context_not_loggedin(self):
		response = self.client.get(reverse('musics:artist_detail', kwargs={'slug':self.entry.slug}))
		context = response.context
		self.assertEqual(response.status_code, 200)
		self.assertNotIn('fav_status', context)