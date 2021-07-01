from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from accounts.models import User
from musics.models import Song, Artist


class BaseSeachListView(ListView):
	def get_queryset(self):
		self.keyword = self.request.GET['keyword']

		qs = super().get_queryset()
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['keyword'] = self.request.GET['keyword']
		return context


class ArtistSearchListView(BaseSeachListView):
	model=Artist
	template_name = 'search/artist.html'

	def get_queryset(self):
		qs = super().get_queryset()
		
		if not self.keyword:
			return qs.none()

		return qs.filter(
			Q(artist_name__icontains = self.keyword) | Q(artist_name_id__icontains = self.keyword)
		)
		


class SongSearchListView(BaseSeachListView):
	model=Song
	template_name = 'search/song.html'

	def get_queryset(self):
		qs = super().get_queryset()

		if not keyword:
			return Song.objects.none()

		return Song.objects.filter(
			Q(song_name__icontains = keyword)
		)


class UserSearchListView(BaseSeachListView):
	template_name = 'search/user.html'

	def get_queryset(self):
		keyword = self.request.GET['keyword']
		
		if not keyword:
			return User.objects.none()

		return User.objects.filter(
			Q(username__icontains = keyword) | Q(handle__icontains = keyword)
		)