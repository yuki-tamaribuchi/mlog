from django.forms import ModelForm

from django_select2 import forms as s2forms
from concurrency.forms import ConcurrentForm

from .models import Artist, Song, Genre


class ArtistWidget(s2forms.ModelSelect2MultipleWidget):
	search_fields = [
		'artist_name__icontains',
		'slug__icontains',
	]


class ArtistBelongToWidget(s2forms.ModelSelect2Widget):
	search_fields = [
		'artist_name__icontains',
		'slug__icontains'
	]


class GenreWidget(s2forms.ModelSelect2MultipleWidget):
	search_fields = [
		'genre_name__icontains'
	]


class ArtsitForm(ConcurrentForm):
	class Meta:
		model = Artist
		fields = ('artist_name', 'genre', 'slug', 'artist_biograph', 'belong_to', 'version')
		widgets = {
			'genre':GenreWidget,
			'belong_to':ArtistBelongToWidget,
		}


class SongForm(ConcurrentForm):
	class Meta:
		model = Song
		fields = ('song_name', 'artist', 'genre', 'spotify_link', 'spotify_preview_url', 'artwork_url', 'version')
		widgets = {
			'artist':ArtistWidget,
			'genre':GenreWidget,
		}


class GenreForm(ModelForm):
	class Meta:
		model = Genre
		fields = ('genre_name',)