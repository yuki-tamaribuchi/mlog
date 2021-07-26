from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

from entry.models import Entry
from favorite_artists.models import FavoriteArtist

from activity.tasks import artist_checked_activity, song_checked_activity, genre_checked_activity

from .models import Artist, Song, Genre
from .forms import ArtsitCreateForm, SongCreateForm, GenreCreateForm


class ArtistDetailView(DetailView):
	template_name = 'musics/artistdetail.html'

	def get_object(self):
		current_artist = Artist.objects.get(artist_name_id=self.kwargs['artist_name_id'])

		artist_checked_activity.delay(self.kwargs['artist_name_id'], self.request.user.username)

		return current_artist

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['entries'] = Entry.objects.filter(song__artist__artist_name_id=self.kwargs['artist_name_id'])

		context['members'] = Artist.objects.filter(belong_to__artist_name_id=self.kwargs['artist_name_id'])

		if self.request.user.username:
			try:
				context['fav_status'] = FavoriteArtist.objects.get(user__username=self.request.user.username, artist__artist_name_id=self.kwargs['artist_name_id'])
			except ObjectDoesNotExist:
				context['fav_status'] = FavoriteArtist.objects.none()

		return context



class SongCreateView(CreateView):
	form_class = SongCreateForm
	template_name = 'musics/songcreate.html'

	def get_success_url(self):
		return reverse_lazy('musics:song_detail', kwargs={'pk':self.object.id})


class ArtistCreateView(CreateView):
	form_class = ArtsitCreateForm
	template_name = 'musics/artistcreate.html'

	def get_success_url(self):
		return reverse_lazy('musics:artist_detail', kwargs={'artist_name_id':self.object.artist_name_id})


class SongDetailView(DetailView):
	template_name = 'musics/songdetail.html'

	def get_object(self):
		current_song = Song.objects.get(pk=self.kwargs['pk'])

		song_checked_activity.delay(self.kwargs['pk'], self.request.user.username)

		return current_song


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['entries'] = Entry.objects.filter(song=self.kwargs['pk'])
		return context


class PopupSongCreateView(SongCreateView):

	def form_valid(self, form):
		song = form.save()
		context = {
			'object_name':str(song),
			'object_pk':song.pk,
			'function_name':'add_song'
		}
		return render(self.request, 'musics/close.html', context)


class PopupArtistCreateView(ArtistCreateView):

	def form_valid(self, form):
		artist = form.save()
		context = {
			'object_name':str(artist),
			'object_pk':artist.pk,
			'function_name':'add_artist'
		}
		return render(self.request, 'musics/close.html', context)


class GenreCreateView(CreateView):
	form_class = GenreCreateForm
	template_name = 'musics/genrecreate.html'


	def get_success_url(self):
		return reverse_lazy('entry:create')


class PopupGenreCreateView(GenreCreateView):

	def form_valid(self, form):
		genre = form.save()
		context = {
			'object_name':str(genre),
			'object_pk':genre.pk,
			'function_name':'add_genre'
		}
		return render(self.request, 'musics/close.html',context)


class GenreListView(ListView):
	model = Genre
	ordering = ['genre_name']
	template_name = 'mlog/genre_list.html'


class ArtistByGenreListView(ListView):
	template_name = 'musics/artist_by_genre_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		genre_checked_activity.delay(self.kwargs['genre_name'], self.request.user.username)
		return qs.filter(genre__genre_name=self.kwargs['genre_name']).order_by('artist_name_id')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['genre'] = Genre.objects.get(genre_name=self.kwargs['genre_name'])
		return context