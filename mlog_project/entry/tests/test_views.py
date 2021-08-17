from django.test import TestCase, RequestFactory
from django.urls import reverse

from utils import utils_for_test

from entry.models import Entry
from entry.views import EntryCreateView

class EntryCreateViewTest(TestCase):

	def setUp(self):
		self.user = utils_for_test.create_test_user(
			username='testuser',
			handle='test user',
			biograph='test biograph',
		)
		self.user.set_password('password')
		self.factory = RequestFactory()
	
	def test_create_template(self):
		request = self.factory.get(reverse('entry:create'))
		request.user = self.user
		response = EntryCreateView.as_view()(request)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/entry_form.html'):
			response.render()


class EntryDetailViewTest(TestCase):

	def setUp(self):
		utils_for_test.create_test_entry(
			title='test title',
			content='test content',
			username='testuser',
			handle='test user',
			biograph='test biograph',
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

	def test_detail_template(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'entry/detail.html')

	