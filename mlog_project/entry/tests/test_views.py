from django.http import response
from django.test import TestCase, RequestFactory
from django.urls import reverse

from accounts.models import User
from musics.models import Song
from likes.models import Like

from utils import utils_for_test

from entry.models import Entry
from entry.views import EntryCreateView, EntryUpdateView, EntryDeleteView, EntryDetailView

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
	
	def test_template(self):
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
		entry = Entry.objects.first()
		self.assertEqual(response.status_code, 302)
	'''


class EntryDetailViewTest(TestCase):

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
		self.user_for_like = utils_for_test.create_test_user(
			username='userforlike',
			handle='user for like',
			biograph='biograph for user for like',
		)

		self.factory = RequestFactory()

	def test_template(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'entry/detail.html')



	def test_context_like_count_assertin(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('like_count', context)

	def test_context_comment_count_assertin(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('comment_count', context)

	def test_context_like_status_assertin(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('like_status', context)


	def test_context_view_count_assertin(self):
		entry = Entry.objects.first()
		response = self.client.get(reverse('entry:detail', kwargs={'pk':entry.id}))
		context = response.context
		self.assertIn('view_count', context)

	def test_like_status_exitst(self):
		like_object = Like.objects.create(
			user=self.user_for_like,
			entry=self.entry
		)
		request = self.factory.get(reverse('entry:detail', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_like
		response = EntryDetailView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.context_data['like_status'], like_object)
		
	def test_like_status_not_exist(self):
		like_object = Like.objects.none()
		request = self.factory.get(reverse('entry:detail', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_like
		response = EntryDetailView.as_view()(request, pk=self.entry.id)
		self.assertQuerysetEqual(response.context_data['like_status'], like_object)

	def test_like_count_one(self):
		Like.objects.create(
			user=self.user_for_like,
			entry=self.entry
		)
		request = self.factory.get(reverse('entry:detail', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_like
		response = EntryDetailView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.context_data['like_count'], 1)

	def test_like_count_zero(self):
		request = self.factory.get(reverse('entry:detail', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_like
		response = EntryDetailView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.context_data['like_count'], 0)


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

	def test_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user
		response = EntryUpdateView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/entry_form.html'):
			response.render()


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

	def test_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user
		response = EntryDeleteView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/delete_confirm.html'):
			response.render()


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
	
	def test_template(self):
		response = self.client.get(reverse('entry:entry_list_by_song', kwargs={'pk':self.song.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('entry/entry_list_by_song.html')
		