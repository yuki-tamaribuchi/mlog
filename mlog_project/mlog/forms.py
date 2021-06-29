from django.db import models
from django.db.models.base import Model
from django.forms import ModelForm, fields

from musics.models import Artist, Genre, Song

from .models import Entry


class EntryCreateForm(ModelForm):
	class Meta:
		model=Entry
		fields=('title','content','song')


class ArtsitCreateForm(ModelForm):
	class Meta:
		model=Artist
		fields=('artist_name','genre','artist_name_id','artist_biograph')


class SongCreateForm(ModelForm):
	class Meta:
		model=Song
		fields=('song_name','artist','genre')


class GenreCreateForm(ModelForm):
	class Meta:
		model=Genre
		fields='__all__'