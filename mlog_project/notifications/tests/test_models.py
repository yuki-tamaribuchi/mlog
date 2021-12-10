from logging import Handler
from django.test import TestCase

from notifications.models import Notifications
from notifications.tasks import add_notification
from accounts.models import User

from utils import utils_for_test

class TestNotification(TestCase):

	def setUp(self):
		self.user_from = utils_for_test.create_test_user(
			username='userfrom',
			handle='user from',
			biograph='test biograph'
		)

		self.content = utils_for_test.create_test_entry(
			title='test entry',
			content='test content',
			username='entryuser',
			handle='entry user',
			biograph='test biograph',
			song_name='test song',
			artist_name='test artist',
			slug='testartist',
			genre_name='test genre'
		)

		self.user_to = User.objects.get(
			username='entryuser'
		)

		add_notification(
			user_from=self.user_from,
			user_to=self.user_to,
			notification_type='like'
		)

	def test_str_method(self):
		notification_instance = Notifications.objects.first()
		self.assertEqual(str(notification_instance), 'From:userfrom, To:entryuser, is-Read:0')