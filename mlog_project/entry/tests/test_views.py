from django.http import request, response
from django.template import context
from django.test import TestCase, RequestFactory
from django.urls import reverse

from accounts.models import User
from musics.models import Artist, Song
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

	def test_success_url(self):
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
		response.client = self.client
		entry = Entry.objects.first()
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, reverse('entry:detail', kwargs={'pk':entry.id}))


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
		self.user_for_request = utils_for_test.create_test_user(
			username='userforrequest',
			handle='user for request',
			biograph='biograph for user for request'
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
		request.user = self.user_for_request
		response = EntryDetailView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.context_data['like_count'], 1)

	def test_like_count_zero(self):
		request = self.factory.get(reverse('entry:detail', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_request
		response = EntryDetailView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.context_data['like_count'], 0)

	def test_get_inactive_users_entry_raised_404(self):
		from django.http import Http404
		self.entry_user = self.entry.writer
		self.entry_user.is_active = False
		self.entry_user.save()
		request = self.factory.get(reverse('entry:detail', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_request
		with self.assertRaises(Http404):
			EntryDetailView.as_view()(request, pk=self.entry.id)


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

		self.writer = self.entry.writer
		self.user_for_request = utils_for_test.create_test_user(
			username='userforrequest',
			handle='user for request',
			biograph='biograph for user for request'
		)
		self.factory = RequestFactory()

	def test_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.writer
		response = EntryUpdateView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/entry_form.html'):
			response.render()
	
	def test_not_writer_try_update_entry_raise_403(self):
		from django.core.exceptions import PermissionDenied
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_request
		with self.assertRaises(PermissionDenied):
			EntryUpdateView.as_view()(request, pk=self.entry.id)

	'''
	def test_success_url(self):
		entry = Entry.objects.first()
		request = self.factory.get(reverse('entry:update', kwargs={'pk':entry.id}))
		request.user = self.user
		response = EntryUpdateView.as_view()(request, pk=entry.id)
		response.client = self.client
		entry_in_response = response.context_data['entry']
		request = self.factory.post(
			path=reverse('entry:update', kwargs={'pk':entry_in_response.id}),
			data={
				'title':entry_in_response.title,
				'content':'canged content',
				'song':entry_in_response.song,
				'writer':entry_in_response.writer,
			}
		)
		request.user = self.user
		response = EntryUpdateView.as_view()(request, pk=entry_in_response.id)
		self.assertEqual(response.status_code, 200)
	'''
	

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

		self.writer = self.entry.writer
		self.user_for_request = utils_for_test.create_test_user(
			username='userforrequest',
			handle='user for request',
			biograph='biograph for user for request'
		)
		self.factory = RequestFactory()

	def test_template(self):
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.writer
		response = EntryDeleteView.as_view()(request, pk=self.entry.id)
		self.assertEqual(response.status_code, 200)
		with self.assertTemplateUsed('entry/delete_confirm.html'):
			response.render()

	def test_not_writer_try_delete_entry_raise_403(self):
		from django.core.exceptions import PermissionDenied
		request = self.factory.get(reverse('entry:update', kwargs={'pk':self.entry.id}))
		request.user = self.user_for_request
		with self.assertRaises(PermissionDenied):
			EntryDeleteView.as_view()(request, pk=self.entry.id)


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

		self.song_for_no_entry = utils_for_test.create_test_song(
			song_name='song for no entry',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre no entry',
		)
	
	def test_template(self):
		response = self.client.get(reverse('entry:entry_list_by_song', kwargs={'pk':self.song.id}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'entry/entry_list.html')

	def test_object_does_not_exist(self):
		object = Entry.objects.none()
		response = self.client.get(reverse('entry:entry_list_by_song', kwargs={'pk':self.song_for_no_entry.id}))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['object_list'], object)


class EntryListByArtistViewTest(TestCase):

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

		self.artist = Artist.objects.first()

		self.artist_for_no_entry = utils_for_test.create_test_artist(
			artist_name='artist for no entry',
			slug='artistfornoentry',
			genre_name='test genre',
		)
	
	def test_template(self):
		response = self.client.get(reverse('entry:entry_list_by_artist', kwargs={'slug':self.artist.slug}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'entry/entry_list.html')

	def test_object_does_not_exist(self):
		object = Entry.objects.none()
		response = self.client.get(reverse('entry:entry_list_by_artist', kwargs={'slug':self.artist_for_no_entry.slug}))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['object_list'], object)