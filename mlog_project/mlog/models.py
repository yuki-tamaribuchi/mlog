from typing_extensions import TypeGuard
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from accounts.models import User

from musics.models import Song


class Entry(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    song=models.ForeignKey(Song,on_delete=models.PROTECT)

    def __str__(self):
        return '%s written by %s (Song:%s)'%(self.title,self.writer,self.song)