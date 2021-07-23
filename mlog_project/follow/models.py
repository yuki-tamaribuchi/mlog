from django.db import models

from accounts.models import User


class Follow(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_user')
	follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='followed_user')

	def __str__(self):
		return '%s follows %s'%(self.user,self.follower)