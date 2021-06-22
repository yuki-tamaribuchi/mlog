import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	def get_image_path(self,filename):
		from uuid import uuid4
		import os

		prefix='accounts/images/profile/'
		name=str(uuid4()).replace('-','')
		ext=os.path.splitext(filename)[-1]
		
		return prefix+name+ext

	handle=models.CharField(max_length=20)
	biograph=models.TextField(max_length=200,blank=True)
	profile_image=models.ImageField(
		upload_to=get_image_path,
		blank=True,
		
		)


class Follow(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_user')
	follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followed_user')

	def __str__(self):
		return '%s follows %s'%(self.user,self.follower)


