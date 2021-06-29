from logging import Handler
from django.test import TestCase

from accounts.models import User

class UserTests(TestCase):

	test_username='test_user'
	test_handle='test handle'
	test_biograph='test biograph'

	@classmethod
	def setUpTestData(cls):
		cls.test_user_instance=User.objects.create(
			username=cls.test_username,
			handle=cls.test_handle,
			biograph=cls.test_biograph,
		)

	def test_handle(self):
		self.assertQuerysetEqual(self.test_user_instance.username, self.test_username)
		self.assertQuerysetEqual(self.test_user_instance.handle, self.test_handle)
		self.assertQuerysetEqual(self.test_user_instance.biograph, self.test_biograph)