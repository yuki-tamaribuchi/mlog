from django.db import models
from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Entry, Comment, Artist, Genre, Song


class EntryCreateForm(ModelForm):
	class Meta:
		model=Entry
		fields=('title','content','song')


class CommentCreateForm(ModelForm):
	class Meta:
		model=Comment
		fields=('comment',)


class ArtsitCreateForm(ModelForm):
	class Meta:
		model=Artist
		fields=('artist_name','genre','subgenre','artist_name_id','artist_biograph')


class SongCreateForm(ModelForm):
	class Meta:
		model=Song
		fields=('song_name','artist','genre','subgenre')


class GenreCreateForm(ModelForm):
	class Meta:
		model=Genre
		fields='__all__'