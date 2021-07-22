from django.test import TestCase

from entry.models import Entry
from accounts.models import User
from musics.models import Genre, Artist, Song

from utils import utils_for_test

class EntryTest(TestCase):

	@classmethod
	def setUp(cls):
		utils_for_test.create_test_entry(
			title='test title',
			content='test content',
			username='testuser',
			handle='test user',
			biograph='test biograph',
			song_name='test song',
			artist_name='test artist',
			artist_name_id='testartist',
			genre_name='test genre'
		)
	
	def test_title_max_length(self):
		entry = Entry.objects.all().first()
		max_length = entry._meta.get_field('title').max_length
		self.assertEqual(max_length, 30)


	'''
	I did't set max length for content.

	def test_content_max_length(self):
		entry = Entry.objects.all().first()
		max_length = entry._meta.get_field('content').max_length
		self.assertEqual(max_length, )
	'''

	def test_str(self):
		entry = Entry.objects.all().first()
		self.assertEqual(str(entry), 'test title written by testuser (Song:test song by test artist)')