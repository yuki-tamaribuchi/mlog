from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	handle=models.CharField(max_length=20)
	biograph=models.TextField(max_length=200)


class Follow(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_user')
	follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followed_user')

	def __str__(self):
		return '%s follows %s'%(self.user,self.follower)


