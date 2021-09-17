from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Follow(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_user', verbose_name=_('user'))
	follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_user', verbose_name=_('follower'))

	def __str__(self):
		return '%s follows %s'%(self.user,self.follower)