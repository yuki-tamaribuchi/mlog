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

from utils import utils_for_test

class TestEntryReadActivity(TestCase):

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


	def test_with_user_str(self):
		read_user_instance = utils_for_test.create_test_user(
			username='testuserforread',
			handle='test user for read',
			biograph='test biograph'
		)
		entry_instance = Entry.objects.first()
		activity_instance = EntryReadActivity.objects.create(user=read_user_instance, entry=entry_instance)
		self.assertEqual(str(activity_instance), 'testuserforread read test title')

	def test_without_user_str(self):
		entry_instance = Entry.objects.first()
		activity_instance = EntryReadActivity.objects.create(user=None, entry=entry_instance)
		self.assertEqual(str(activity_instance), 'Unknown user read test title')


class TestArtistCheckedActivity(TestCase):

	@classmethod
	def setUp(cls):
		test_artist = utils_for_test.create_test_artist(
			artist_name='test artist',
			artist_name_id='testartist',
			genre_name='test genre',
		)

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
		test_song = utils_for_test.create_test_song(
			song_name='test song',
			artist_name='test artist',
			artist_name_id='testartist',
			genre_name='test genre'
		)

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

		test_detail_user = utils_for_test.create_test_user(
			username='testdetailuser',
			handle='test detail user',
			biograph='test biograph'
		)

		test_user_for_activity = utils_for_test.create_test_user(
			username='testuserforact',
			handle='test user for act',
			biograph='test biograph'
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