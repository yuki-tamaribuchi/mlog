from django.test import TestCase

from accounts.models import User
from follow.models import Follow

class TestFollow(TestCase):

	@classmethod
	def setUp(cls):

		test_follow_user = User.objects.create(
			username = 'testfollowuser',
			handle = 'test follow user'
		)

		test_follower_user = User.objects.create(
			username = 'testfolloweruser',
			handle = 'test follower user'
		)

		Follow.objects.create(
			user = test_follow_user,
			follower = test_follower_user
		)
	
	def test_str(self):
		follow_instance = Follow.objects.all().first()
		self.assertEqual(str(follow_instance), 'testfollowuser follows testfolloweruser')