from django.test import TestCase
from django.urls import resolve

from mlog import views

class TestMlogUrls(TestCase):

	def test_top(self):
		view = resolve('/top/')
		self.assertEqual(view.func.view_class, views.TopView)

	def test_timeline(self):
		view = resolve('/timeline/')
		self.assertEqual(view.func.view_class, views.TimelineView)