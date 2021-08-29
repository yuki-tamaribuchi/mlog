from django.db import models

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

	category = models.CharField(max_length=3, choices=CONTACT_CATEGORY_CHOICES)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s by %s'%(self.category, self.user.username)