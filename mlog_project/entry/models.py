from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from musics.models import Song
from accounts.models import User


class Entry(models.Model):
	title = models.CharField(verbose_name=_('title'), max_length=30)
	content = models.TextField(_('content'))
	writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entrys_writer' ,verbose_name=_('writer'))
	created_at = models.DateTimeField(verbose_name=_('created at'))
	updated_at = models.DateTimeField(verbose_name=_('updated at'))
	song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='featured_song', verbose_name=_('song'))

	def save(self, *args, **kwargs):
		if not self.id:
			self.created_at = timezone.now()
		self.updated_at = timezone.now()
		return super(Entry, self).save(*args, **kwargs)

	def __str__(self):
	    return '%s written by %s (Song:%s)'%(self.title, self.writer,self.song)