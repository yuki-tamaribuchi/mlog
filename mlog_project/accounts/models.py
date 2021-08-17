from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	def get_image_path(self,filename):
		from uuid import uuid4
		import os

		prefix = 'images/users/accounts/profile/'
		name = str(uuid4()).replace('-', '')
		ext = os.path.splitext(filename)[-1]
		
		return prefix + name + ext

	handle = models.CharField(max_length=20)
	biograph = models.TextField(max_length=200, blank=True)
	profile_image = models.ImageField(
		upload_to=get_image_path,
		default='images/defaults/accounts/profile/default.jpg'
		)