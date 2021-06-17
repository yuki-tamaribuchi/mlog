from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Entry, Comment


class EntryCreateForm(ModelForm):
	class Meta:
		model=Entry
		fields=('title','content','song')


class CommentCreateForm(ModelForm):
	class Meta:
		model=Comment
		fields=('comment',)