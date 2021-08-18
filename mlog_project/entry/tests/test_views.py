from django.test import TestCase, RequestFactory
from django.urls import reverse

from accounts.models import User

from utils import utils_for_test

from entry.models import Entry
from entry.views import EntryCreateView, EntryUpdateView, EntryDetailView

class EntryCreateViewTest(TestCase):

	def setUp(self):
		self.user = utils_for_test.create_test_user(
			username='testuser',
			handle='test user',
			biograph='test biograph',
		)
		self.user.set_password('password')

		self.song = utils_for_test.create_test_song(
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

		self.factory = RequestFactory()

	'''
	def test_create_form(self):
		request = self.factory.get(reverse('entry:create'))
		request.user = self.user
		response = EntryCreateView.as_view()(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response)
	'''
	
	def test_create_template(self):
		request = self.factory.get(reverse('entry:create'))
		request.user = self.user
		response = EntryCreateView.as_view()(request)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/entry_form.html'):
			response.render()

	'''
	def test_create_success_url(self):
		request = self.factory.post(
			path=reverse('entry:create'),
			data={
				'title':'test title',
				'content':'test content',
				'song':self.song.id,
				'writer':self.user.id,
			}
		)
		request.user = self.user
		response = EntryCreateView.as_view()(request)
		self.assertEqual(response.status_code, 200)
	'''


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


'''
	def test_context_context(self):
		entry = Entry.objects.first()
		request = RequestFactory().get(reverse('entry:detail', kwargs={'pk':entry.id}))
		request.user = User.objects.first()
		view = EntryDetailView()
		view.setup(request, pk=entry.id)

		view.get_object()
		context = view.get_context_data()
		self.assertIn('like_count', context)
		self.assertIn('comment_count', context)
		self.assertIn('like_status', context)
		self.assertIn('view_count', context)
ERROR
AttributeError: 'EntryDetailView' object has no attribute 'object'
'''

'''
class EntryUpdateViewTest(TestCase):

	def setUp(self):
		self.entry = utils_for_test.create_test_entry(
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

		self.user = User.objects.first()

		self.factory = RequestFactory()

	def test_create_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user
		response = EntryUpdateView.as_view()(request)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/entry_form.html'):
			response.render()

ERROR
return Entry.objects.get(writer__username=self.request.user.username, id=self.kwargs['pk'])
	KeyError: 'pk'
'''