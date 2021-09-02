from datetime import time
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import User

MLOG = 'MLG'
ACCOUNT = 'ACC'
ARTIST = 'ART'
SONG = 'SON'
USER = 'USR'
ENTRY = 'ENT'

CONTACT_CATEGORY_CHOICES = (
	(MLOG, 'このサービスについて'),
	(ACCOUNT, 'アカウントについて'),
	(ARTIST, 'アーティストについて'),
	(SONG, '曲について'),
	(USER, 'ユーザについて'),
	(ENTRY, 'エントリについて'),
)

class ContactThreads(models.Model):

	category = models.CharField(verbose_name=_('category'), max_length=3, choices=CONTACT_CATEGORY_CHOICES)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(verbose_name=_('created at'), auto_now=True)

	def __str__(self):
		return '%s by %s'%(self.category, self.user.username)


class ContactContent(models.Model):

	parent_thread = models.ForeignKey(ContactThreads, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.created_at = timezone.now()
		self.updated_at = timezone.now()
		return super(ContactContent, self).save(*args, **kwargs)

	def __str__(self):
		return 'Content from %s to %s by %s'%(self.user.username, self.parent_thread.category, self.parent_thread.user)