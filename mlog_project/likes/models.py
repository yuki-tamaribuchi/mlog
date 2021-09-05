from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from entry.models import Entry


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE, verbose_name=_('entry'))

	def __str__(self):
		return '%s liked %s'%(self.user,self.entry)