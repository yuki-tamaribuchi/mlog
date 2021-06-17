from typing_extensions import TypeGuard
from django.db import models
from django.db.models.base import Model
from accounts.models import User


class Genre(models.Model):
    genre_name=models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name


class SubGenre(models.Model):
    subgenre_name=models.CharField(max_length=20)
    main_genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self):
        return self.subgenre_name


class Artist(models.Model):
    artist_name=models.CharField(max_length=30)
    genre=models.ManyToManyField(Genre)
    subgenre=models.ManyToManyField(SubGenre,blank=True)
    artist_name_id=models.CharField(max_length=30,null=True)
    artist_biograph=models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.artist_name


class Song(models.Model):
    song_name=models.CharField(max_length=30)
    artist=models.ManyToManyField(Artist)
    genre=models.ManyToManyField(Genre)
    subgenre=models.ManyToManyField(SubGenre,blank=True)


    def __str__(self):
        return '%s by %s'%(self.song_name,self.artist)


class Entry(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    song=models.ForeignKey(Song,on_delete=models.PROTECT)

    def __str__(self):
        return '%s written by %s (Song:%s)'%(self.title,self.writer,self.song)


class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    entry=models.ForeignKey(Entry,on_delete=models.CASCADE)

    def __str__(self):
        return '%s liked %s'%(self.user,self.entry)


class Comment(models.Model):
    comment=models.TextField(max_length=200)
    entry=models.ForeignKey(Entry,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)