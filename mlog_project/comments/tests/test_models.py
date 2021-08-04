from django.test import TestCase

from comments.models import Comment
from musics.models import Genre, Song, Artist
from entry.models import Entry
from accounts.models import User

from utils import utils_for_test


class CommentTests(TestCase):

	@classmethod
	def setUp(cls):
		test_entry = utils_for_test.create_test_entry(
			title='test title',
			content='test content',
			username='testuserforentry',
			handle='test entry for entry',
			biograph='test biograph',
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

		test_user_for_comment = utils_for_test.create_test_user(
			username='testuserforcomment',
			handle='testuser for comment',
			biograph='test biograph'
		)
		
		Comment.objects.create(
			comment = 'test comment',
			entry = test_entry,
			user = test_user_for_comment,
		)


	def test_comment_max_length(self):
		comment = Comment.objects.all().first()
		max_length = comment._meta.get_field('comment').max_length
		self.assertEqual(max_length, 200)


	def test_str(self):
		comment = Comment.objects.all().first()
		self.assertEqual(str(comment), 'testuserforcomment comment to test title')