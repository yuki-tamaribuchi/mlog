from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from entry.models import Entry

class Comment(models.Model):
	comment = models.TextField(verbose_name=_('comment'), max_length=200)
	entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '%s comment to %s'%(self.user.username, self.entry.title)