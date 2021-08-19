from django.http import response
from django.template import context
from django.test import TestCase, RequestFactory
from django.urls import reverse

from accounts.models import User
from musics.models import Song

from utils import utils_for_test

from entry.models import Entry
from entry.views import EntryCreateView, EntryUpdateView, EntryDetailView, EntryDeleteView

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



	def test_context_like_count(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('like_count', context)

	def test_context_comment_count(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('comment_count', context)

	def test_context_like_status(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('like_status', context)


	def test_context_view_count(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('view_count', context)


'''
QUERY DOESN'T MATCH

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

		self.user = User.objects.get(username='testuser')

		self.factory = RequestFactory()

	def test_create_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user
		response = EntryUpdateView.as_view()(request, kwargs={'pk':self.entry.id})
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/entry_form.html'):
			response.render()
'''

'''
QUERY DOESN'T MATCH

class EntryDeleteViewTest(TestCase):
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

		self.user = User.objects.get(username='testuser')

		self.factory = RequestFactory()

	def test_create_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user
		response = EntryDeleteView.as_view()(request, kwargs={'pk':self.entry.id})
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/delete_confirm.html'):
			response.render()
'''


class EntryListBySongViewTest(TestCase):

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

		self.song = Song.objects.first()
	
	def test_list_template(self):
		response = self.client.get(reverse('entry:entry_list_by_song', kwargs={'pk':self.song.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('entry/entry_list_by_song.html')
		