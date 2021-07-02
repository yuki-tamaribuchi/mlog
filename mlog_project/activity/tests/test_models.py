from django.test import TestCase

from accounts.models import User
from entry.models import Entry
from musics.models import Artist, Song, Genre
from activity.models import (
	EntryReadActivity,
	ArtistCheckedActivity,
	SongCheckedActivity,
	UserDetailCheckedActivity,
	GenreCheckedActivity,
)

class TestEntryReadActivity(TestCase):

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

		test_user_for_activity = User.objects.create(
			username = 'testuserforact',
			handle = 'testuser for act',
		)

		EntryReadActivity.objects.create(
			user = test_user_for_activity,
			entry = test_entry
		)

	def test_str(self):
		activity_instance = EntryReadActivity.objects.all().first()
		self.assertEqual(str(activity_instance), 'testuserforact read test title')


class TestArtistCheckedActivity(TestCase):

	@classmethod
	def setUp(cls):
		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_artist = Artist.objects.create(
			artist_name = 'test artist',
			artist_name_id = 'testartist',
		)
		test_artist.genre.add(test_genre)

		test_user_for_activity = User.objects.create(
			username = 'testuserforact',
			handle = 'testuser for act',
		)

		ArtistCheckedActivity.objects.create(
			user = test_user_for_activity,
			artist = test_artist,
		)

	def test_str(self):
		activity_instance = ArtistCheckedActivity.objects.all().first()
		self.assertEqual(str(activity_instance), 'testuserforact checked test artist')

	
class TestSongCheckedActivity(TestCase):

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

		test_user_for_activity = User.objects.create(
			username = 'testuserforact',
			handle = 'testuser for act',
		)

		ArtistCheckedActivity.objects.create(
			user = test_user_for_activity,
			artist = test_artist,
		)
	
	def test_str(self):
		activity_instance = ArtistCheckedActivity.objects.all().first()
		self.assertEqual(str(activity_instance), 'testuserforact checked test artist')


class TestSongCheckedActivity(TestCase):

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

		test_user_for_activity = User.objects.create(
			username = 'testuserforact',
			handle = 'testuser for act',
		)

		SongCheckedActivity.objects.create(
			user = test_user_for_activity,
			song = test_song
		)

	def test_str(self):
		activity_instance = SongCheckedActivity.objects.all().first()
		self.assertEqual(str(activity_instance), 'testuserforact checked test song')


class TestUserCheckedActivity(TestCase):

	@classmethod
	def setUp(cls):

		test_detail_user = User.objects.create(
			username = 'testdetailuser',
			handle = 'test detail user',
		)

		test_user_for_activity = User.objects.create(
			username = 'testuserforact',
			handle = 'testuser for act',
		)

		UserDetailCheckedActivity.objects.create(
			user = test_user_for_activity,
			detail_user = test_detail_user,
		)

	def test_str(self):
		activity_instance = UserDetailCheckedActivity.objects.all().first()
		self.assertEqual(str(activity_instance), 'testuserforact checked testdetailuser')


class TestGenreCheckedActivity(TestCase):

	@classmethod
	def setUp(cls):
		test_genre = Genre.objects.create(genre_name = 'test genre')

		test_user_for_activity = User.objects.create(
			username = 'testuserforact',
			handle = 'testuser for act',
		)

		GenreCheckedActivity.objects.create(
			user = test_user_for_activity,
			genre = test_genre,
		)

	def test_str(self):
		activity_instance = GenreCheckedActivity.objects.all().first()
		self.assertEqual(str(activity_instance), 'testuserforact checked test genre')