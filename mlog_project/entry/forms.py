from django.forms import ModelForm

from django_select2 import forms as s2forms

from .models import Entry


class SongWidget(s2forms.ModelSelect2Widget):
	search_fields = [
		'song_name__icontains',
		'artist__artist_name__icontains'
	]


class EntryCreateForm(ModelForm):
	class Meta:
		model = Entry
		fields = ('title', 'content', 'song')
		widgets = {
			'song':SongWidget,
		}