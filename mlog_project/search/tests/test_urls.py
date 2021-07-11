from django.test import TestCase
from django.urls import resolve

from search import views

class TestSearchUrls(TestCase):
	
	def test_artist(self):
		view = resolve('/search/artist/')
		self.assertEqual(view.func.view_class, views.ArtistSearchListView)

	def test_song(self):
		view = resolve('/search/song/')
		self.assertEqual(view.func.view_class, views.SongSearchListView)

	def test_user(self):
		view = resolve('/search/user/')
		self.assertEqual(view.func.view_class, views.UserSearchListView)