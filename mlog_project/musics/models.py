from django.db import models


class Genre(models.Model):
    genre_name=models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name


class Artist(models.Model):
    artist_name=models.CharField(max_length=30)
    genre=models.ManyToManyField(Genre)
    artist_name_id=models.CharField(max_length=30,unique=True)
    artist_biograph=models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.artist_name


class Song(models.Model):
    song_name=models.CharField(max_length=30)
    artist=models.ManyToManyField(Artist)
    genre=models.ManyToManyField(Genre)

    def __str__(self):
        names=[name.artist_name for name in self.artist.all()]
        return '%s by %s'%(self.song_name,str(names))