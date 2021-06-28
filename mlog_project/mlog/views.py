from typing import List
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.expressions import OrderBy
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.db.models import Q

from .models import Artist, Entry, Genre, Song
from .forms import EntryCreateForm, SongCreateForm, ArtsitCreateForm, GenreCreateForm
from accounts.models import User
from comments.models import Comment
from likes.models import Like
from favorite_artists.models import FavoriteArtist
from follow.models import Follow
from activity.models import ArtistCheckedActivity, EntryReadActivity, SongCheckedActivity
from utils.utils import get_profile_image_size


class RootRedirectView(View):
	def get(self,request):
		if request.user.username:
			return redirect('mlog:timeline')
		else:
			return redirect('mlog:top')


class TopView(ListView):
	model=Entry
	template_name='mlog/topview.html'
	paginate_by=10

	def get_queryset(self):
		try:
			qs=Entry.objects.all().order_by('-id')
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['profile_image_size']=get_profile_image_size('SM')
		return context


class TimelineView(LoginRequiredMixin, ListView):
	model=Entry
	template_name='mlog/timeline.html'

	def get_queryset(self):
		follows=Follow.objects.filter(user__username=self.request.user.username).values('follower__username')
		
		try:
			qs=Entry.objects.filter(writer__username__in=follows)
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['profile_image_size']=get_profile_image_size('SM')
		return context


class EntryDetailView(DetailView):
	template_name='mlog/entrydetail.html'

	def get_object(self):
		current_entry=get_object_or_404(Entry,id=self.kwargs['pk'])

		if self.request.user.username:
			current_user=User.objects.get(username=self.request.user.username)
			EntryReadActivity.objects.create(user=current_user,entry=current_entry)
		else:
			EntryReadActivity.objects.create(entry=current_entry)

		return current_entry

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['like_count']=Like.objects.filter(entry=self.kwargs['pk']).count()
		context['comment_count']=Comment.objects.filter(entry=self.kwargs['pk']).count()
		context['profile_image_size']=get_profile_image_size('SM')
		
		try:
			context['like_status']=Like.objects.filter(user__username=self.request.user.username,entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			context['like_status']=Like.objects.none()

		context['view_count']=EntryReadActivity.objects.filter(entry__id=self.kwargs['pk']).count()

		return context


class ArtistDetailView(DetailView):
	template_name='mlog/artistdetail.html'

	def get_object(self):
		current_artist=get_object_or_404(Artist,artist_name_id=self.kwargs['artist_name_id'])

		if self.request.user.username:
			current_user=User.objects.get(username=self.request.user.username)
			ArtistCheckedActivity.objects.create(user=current_user,artist=current_artist)

		return current_artist

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['entries']=Entry.objects.filter(song__artist__artist_name_id=self.kwargs['artist_name_id'])

		if self.request.user.username:
			try:
				context['fav_status']=FavoriteArtist.objects.get(user__username=self.request.user.username,artist__artist_name_id=self.kwargs['artist_name_id'])
			except ObjectDoesNotExist:
				context['fav_status']=FavoriteArtist.objects.none()

		return context

class EntryCreateView(LoginRequiredMixin,CreateView):
	form_class=EntryCreateForm
	template_name='mlog/entrycreate.html'

	def form_valid(self, form):
		form.instance.writer_id=User.objects.get(username=self.request.user.username).id
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('mlog:detail',kwargs={'pk':self.object.id})


class SongCreateView(CreateView):
	form_class=SongCreateForm
	template_name='mlog/songcreate.html'

	def get_success_url(self):
		return reverse_lazy('mlog:songdetail',kwargs={'pk':self.object.id})


class ArtistCreateView(CreateView):
	form_class=ArtsitCreateForm
	template_name='mlog/artistcreate.html'

	def get_success_url(self):
		return reverse_lazy('mlog:artistdetail',kwargs={'artist_name_id':self.object.artist_name_id})


class SongDetailView(DetailView):
	template_name='mlog/songdetail.html'

	def get_object(self):
		current_song=Song.objects.get(pk=self.kwargs['pk'])

		if self.request.user.username:
			current_user=User.objects.get(username=self.request.user.username)
			SongCheckedActivity.objects.create(user=current_user, song=current_song)

		return current_song



	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['entries']=Entry.objects.filter(song=self.kwargs['pk'])
		return context


class EntryUpdateView(LoginRequiredMixin, UpdateView):
	template_name='mlog/entryupdate.html'
	fields=('title','content','song')

	def get_object(self):
		return get_object_or_404(Entry,writer__username=self.request.user.username,id=self.kwargs['pk'])


class EntryDeleteView(LoginRequiredMixin, DeleteView):
	template_name='mlog/entrydelete_confirm.html'

	def get_object(self):
		return get_object_or_404(Entry, writer__username=self.request.user.username,id=self.kwargs['pk'])

	def get_success_url(self):
		return reverse_lazy('accounts:detail',kwargs={'username':self.request.user.username})


class PopupSongCreateView(SongCreateView):

	def form_valid(self, form):
		song=form.save()
		context={
			'object_name':str(song),
			'object_pk':song.pk,
			'function_name':'add_song'
		}
		return render(self.request,'mlog/close.html',context)


class PopupArtistCreateView(ArtistCreateView):

	def form_valid(self, form):
		artist=form.save()
		context={
			'object_name':str(artist),
			'object_pk':artist.pk,
			'function_name':'add_artist'
		}
		return render(self.request,'mlog/close.html',context)


class GenreCreateView(CreateView):
	form_class=GenreCreateForm
	template_name='mlog/genrecreate.html'


	def get_success_url(self):
		return reverse_lazy('mlog:entrycreate')


class PopupGenreCreateView(GenreCreateView):

	def form_valid(self, form):
		genre=form.save()
		context={
			'object_name':str(genre),
			'object_pk':genre.pk,
			'function_name':'add_genre'
		}
		return render(self.request,'mlog/close.html',context)


class GenreListView(ListView):
	model=Genre
	ordering=['genre_name']
	template_name='mlog/genre_list.html'


class ArtistByGenreListView(ListView):
	template_name='mlog/artist_by_genre_list.html'

	def get_queryset(self):
		qs=Artist.objects.filter(genre__genre_name=self.kwargs['genre_name']).order_by('artist_name_id')
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['genre']=Genre.objects.get(genre_name=self.kwargs['genre_name'])
		return context