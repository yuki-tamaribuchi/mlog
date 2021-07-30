from django.db import models

from accounts.models import User
from entry.models import Entry


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

	def __str__(self):
		return '%s liked %s'%(self.user,self.entry)