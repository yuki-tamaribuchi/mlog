from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from mlog.models import Artist, Song
from accounts.models import User


class ArtistSearchListView(ListView):
	template_name='mlog/artistsearch.html'

	def get_queryset(self):
		keyword=self.request.GET['keyword']

		if not keyword:
			return Artist.objects.none()

		return Artist.objects.filter(
			Q(artist_name__icontains=keyword) | Q(artist_name_id__icontains=keyword)
		)

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['keyword']=self.request.GET['keyword']
		return context


class SongSearchListView(ListView):
	template_name='mlog/songsearch.html'

	def get_queryset(self):
		keyword=self.request.GET['keyword']

		if not keyword:
			return Song.objects.none()

		return Song.objects.filter(
			Q(song_name__icontains=keyword)
		)
		
	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['keyword']=self.request.GET['keyword']
		return context


class UserSearchListView(ListView):
	template_name='accounts/usersearch.html'

	def get_queryset(self):
		keyword=self.request.GET['keyword']
		
		if not keyword:
			return User.objects.none()

		return User.objects.filter(
			Q(username__icontains=keyword) | Q(handle__icontains=keyword)
		)

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['keyword']=self.request.GET['keyword']
		return context