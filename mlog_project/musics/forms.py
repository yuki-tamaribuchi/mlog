from django.forms import ModelForm

from .models import Artist, Song, Genre

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