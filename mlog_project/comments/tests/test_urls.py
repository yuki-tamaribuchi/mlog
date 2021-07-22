from django.test import TestCase
from django.urls import resolve

from comments import views
import entry.models
import musics.models
import accounts.models

from utils import utils_for_test

class TestCommentsUrls(TestCase):

	@classmethod
	def setUp(cls):
		utils_for_test.create_test_entry(
			title='test title',
			content='test content',
			username='testuserforentry',
			handle='testuser for entry',
			biograph='test biograph',
			song_name='test song',
			artist_name='test artist',
			artist_name_id='testartist',
			genre_name='test genre'
		)
	
	def test_create(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/comments/create/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.CommentCreateView)

	def test_list(self):
		entry_instance = entry.models.Entry.objects.first()
		pk = entry_instance.pk
		view = resolve('/comments/list/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.CommentListView)