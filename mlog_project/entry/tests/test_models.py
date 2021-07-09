from django.test import TestCase

from entry.models import Entry
from accounts.models import User
from musics.models import Genre, Artist, Song


class EntryTest(TestCase):

	@classmethod
	def setUp(cls):

		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_artist = Artist.objects.create(
			artist_name = 'test artist',
			artist_name_id = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_song = Song.objects.create(song_name = 'test song')
		test_song.artist.add(test_artist)
		test_song.genre.add(test_genre)

		test_user_for_entry = User.objects.create(
			username = 'testuserforentry',
			handle = 'testuser for entry',
		)

		Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = test_song,
			writer = test_user_for_entry
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
		self.assertEqual(str(entry), 'test title written by testuserforentry (Song:test song by test artist)')