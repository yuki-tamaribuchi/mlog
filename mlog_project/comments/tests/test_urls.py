from django.test import TestCase
from django.urls import resolve

from comments import views
import entry.models
import comments.models

from utils import utils_for_test


class TestCommentsUrls(TestCase):

	@classmethod
	def setUp(cls):
		utils_for_test.create_test_comment(
			comment='test comment',
			username_for_comment='testuserforcmnt',
			handle_for_comment='test user for cmnt',
			biograph_for_comment='test biograph',
			title='test title',
			content='test content',
			username_for_entry='testuserforentry',
			handle_for_entry='test user for entry',
			biograph_for_entry='test biograph',
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre',
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
	
	def test_update(self):
		comment_instance = comments.models.Comment.objects.first()
		pk = comment_instance.pk
		view = resolve('/comments/update/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.CommentUpdateView)

	def test_delete(self):
		comment_instance = comments.models.Comment.objects.first()
		pk = comment_instance.pk
		view = resolve('/comments/delete/%s/'%(pk))
		self.assertEqual(view.func.view_class, views.CommentDeleteView)