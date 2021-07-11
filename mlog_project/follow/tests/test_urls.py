from django.test import TestCase
from django.urls import resolve

from follow import views
import accounts.models
import follow.models

class TestFollowUrls(TestCase):
	@classmethod
	def setUp(cls):

		test_follow_user = accounts.models.User.objects.create(
			username = 'testfollowuser',
			handle = 'test follow user'
		)

		test_follower_user = accounts.models.User.objects.create(
			username = 'testfolloweruser',
			handle = 'test follower user'
		)

		follow.models.Follow.objects.create(
			user = test_follow_user,
			follower = test_follower_user
		)
	
	def test_process(self):
		view = resolve('/follow/process/')
		self.assertEqual(view.func.view_class, views.FollowProcess)
	
	def test_following_list(self):
		view = resolve('/follow/following/testfollowuser/')
		self.assertEqual(view.func.view_class, views.FollowingListView)

	def test_follower_list(self):
		view = resolve('/follow/follower/testfolloweruser/')
		self.assertEqual(view.func.view_class, views.FollowerListView)