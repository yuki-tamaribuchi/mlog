from django.forms import ModelForm

from django_select2 import forms as s2forms

from .models import Artist, Song, Genre


class ArtistWidget(s2forms.ModelSelect2MultipleWidget):
	search_fields = [
		'artist_name__icontains',
		'artist_name_id__icontains',
	]


class GenreWidget(s2forms.ModelSelect2MultipleWidget):
	search_fields = [
		'genre_name__icontains'
	]


class ArtsitCreateForm(ModelForm):
	class Meta:
		model = Artist
		fields = ('artist_name', 'genre', 'artist_name_id', 'artist_biograph')
		widgets = {
			'genre':GenreWidget,
			'belong_to':ArtistWidget,
		}


class SongCreateForm(ModelForm):
	class Meta:
		model = Song
		fields = ('song_name', 'artist', 'genre')
		widgets = {
			'artist':ArtistWidget,
			'genre':GenreWidget,
		}


class GenreCreateForm(ModelForm):
	class Meta:
		model = Genre
		fields = '__all__'