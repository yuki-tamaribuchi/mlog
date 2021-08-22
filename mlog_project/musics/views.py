from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.db.models import Prefetch, Q

from entry.models import Entry
from favorite_artists.models import FavoriteArtist
from activity.models import SongCheckedActivity

from activity.tasks import artist_checked_activity, song_checked_activity, genre_checked_activity

from .models import Artist, Song, Genre
from .forms import ArtsitForm, SongForm, GenreForm
from .spotify_utils import GetSpotifyData


class ArtistDetailView(DetailView):
	model = Artist
	template_name = 'musics/artist_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['entries'] = Entry.objects.filter(
			song__artist__slug=self.kwargs['slug']
			).select_related(
				'writer',
				'song'
			)


		context['members'] = Artist.objects.filter(belong_to__slug=self.kwargs['slug'])

		context['song_list'] = Song.objects.filter(
			artist__slug=self.kwargs['slug']
			).order_by(
				'song_name'
				).prefetch_related(
					Prefetch(
						'artist',
						queryset=Artist.objects.filter(
							Q(belong_to__slug=self.kwargs['slug']) | Q(slug=self.kwargs['slug'])
						)
					)
				)[:4]

		if self.request.user.username:
			try:
				context['fav_status'] = FavoriteArtist.objects.get(user__username=self.request.user.username, artist__slug=self.kwargs['slug'])
			except ObjectDoesNotExist:
				context['fav_status'] = FavoriteArtist.objects.none()

		return context



class SongCreateView(CreateView):
	form_class = SongForm
	template_name = 'musics/song_form.html'

	def get_success_url(self):
		return reverse_lazy('musics:song_detail', kwargs={'pk':self.object.id})


class ArtistCreateView(CreateView):
	form_class = ArtsitForm
	template_name = 'musics/artist_form.html'

	def get_success_url(self):
		return reverse_lazy('musics:artist_detail', kwargs={'slug':self.object.slug})


class SongDetailView(DetailView):
	template_name = 'musics/song_detail.html'

	def get_object(self):
		current_song = Song.objects.get(pk=self.kwargs['pk'])

		song_checked_activity.delay(self.kwargs['pk'], self.request.user.username)

		return current_song


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['entries'] = Entry.objects.filter(song=self.kwargs['pk'])[:3]
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
		artist=form.save()
		context={
			'object_name':str(artist),
			'object_pk':artist.pk,
			'function_name':'add_artist'
		}
		return render(self.request, 'musics/close.html', context)


class GenreCreateView(CreateView):
	form_class = GenreForm
	template_name = 'musics/genre_form.html'

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
		return render(self.request, 'musics/close.html', context)


class GenreListView(ListView):
	model = Genre
	ordering = ['genre_name']
	template_name = 'mlog/genre_list.html'


class ArtistByGenreListView(ListView):
	model = Artist
	template_name = 'musics/artist_by_genre_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		genre_checked_activity.delay(self.kwargs['genre_name'], self.request.user.username)
		return qs.filter(genre__genre_name=self.kwargs['genre_name']).order_by('slug')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['genre'] = Genre.objects.get(genre_name=self.kwargs['genre_name'])
		return context


class ArtistUpdateView(UpdateView):
	form_class = ArtsitForm
	template_name = 'musics/artist_form.html'

	def get_object(self):
		return Artist.objects.get(slug=self.kwargs['slug'])


class SongUpdateView(UpdateView):
	form_class = SongForm
	template_name = 'musics/song_form.html'

	def get_object(self):
		return Song.objects.get(pk=self.kwargs['pk'])

	def get_success_url(self):
		return reverse_lazy('musics:song_detail', kwargs={'pk':self.object.id})


class SongByArtistListView(ListView):
	model = Song
	template_name = 'musics/song_by_artist_list.html'
	paginate_by = 20

	def get_queryset(self):
		qs = super().get_queryset()
		return qs.filter(artist__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['artist'] = Artist.objects.get(slug=self.kwargs['slug'])
		return context


def search_spotify_tracks(request):
	if request.method=='POST':
		search_keywords = request.POST.get('search_keywords')
		sp = GetSpotifyData()
		results = sp.search_track(search_keywords)
		d = {
			'results':results,
		}
		return JsonResponse(d)


def select_spotify_tracks(request):
	import json
	
	if request.method=='GET':
		return render(request, 'musics/spotify_track_select.html')

	if request.method=='POST':
		selected_track = json.loads(request.POST['selected_track'])
		spotify_link = selected_track['spotify_link']
		preview_url = selected_track['preview_url']
		artwork_url = selected_track['artwork_url']
		context = {
			'spotify_link':spotify_link,
			'preview_url':preview_url,
			'artwork_url':artwork_url,
		}
		return render(request, 'musics/close_select_spotify_tracks.html', context)