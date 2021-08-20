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