from logging import Handler
from django.test import TestCase

from accounts.models import User

class UserTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		User.objects.create(
			username='testuser',
			handle='testhandle',
			biograph='testbiograph',
			profile_image='test.jpg'
		)
	

	def test_handle_max_length(self):
		user=User.objects.get(pk=1)
		max_length=user._meta.get_field('handle').max_length
		self.assertEqual(max_length, 20)

	def test_biograph_max_length(self):
		user=User.objects.get(pk=1)
		max_length=user._meta.get_field('biograph').max_length
		self.assertEqual(max_length, 200)

'''
	How can I write test for profile image.

	def test_get_image_path(self):
		user=User.objects.get(pk=1)
		path=user._meta.get_field('profile_image').upload_to
		print(path)
'''
