from django.test import TestCase

from comments.models import Comment
from musics.models import Genre, Song, Artist
from entry.models import Entry
from accounts.models import User


class CommentTests(TestCase):

	@classmethod
	def setUp(cls):

		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_artist = Artist.objects.create(
			artist_name = 'test artist',
			artist_name_id = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_song = Song.objects.create(song_name = 'song name')
		test_song.artist.add(test_artist)
		test_song.genre.add(test_genre)

		test_user_for_entry = User.objects.create(
			username='testuserforentry',
			handle='testuser for entry',
		)

		test_entry = Entry.objects.create(
			title = 'test title',
			content = 'test content',
			song = test_song,
			writer = test_user_for_entry
		)

		test_user_for_comment = User.objects.create(
			username='testuserforcomment',
			handle='testuser for comment',
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