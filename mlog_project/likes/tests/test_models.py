from django.test import TestCase

from accounts.models import User
from entry.models import Entry
from musics.models import Genre, Artist, Song
from likes.models import Like


class TestLike(TestCase):

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

		test_entry = Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = test_song,
			writer = test_user_for_entry
		)

		test_user_for_like = User.objects.create(
			username = 'testuserforlike',
			handle = 'testuser for like',
		)

		Like.objects.create(
			user = test_user_for_like,
			entry = test_entry
		)

	
	def test_str(self):
		like_instance=Like.objects.all().first()
		self.assertEqual(str(like_instance), 'testuserforlike liked test title written by testuserforentry (Song:test song by [\'test artist\'])')