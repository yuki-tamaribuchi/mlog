from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Entry, Comment, Artist, Song


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
		fields=('artistname','genre','subgenre','artist_name_id','artist_biograph')