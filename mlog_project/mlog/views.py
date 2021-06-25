from typing import List
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.db.models import Q

from .models import Artist, ArtistCheckedHistory, Entry, Like, Comment, Song, ReadHistory, FavoriteArtist
from .forms import EntryCreateForm, CommentCreateForm, SongCreateForm, ArtsitCreateForm, GenreCreateForm
from accounts.models import User, Follow


PROFILE_IMAGE_SIZE={
	'SM':{
		'HEIGHT':100,
		'WIDTH':100
	},
	'MID':{
		'HEIGHT':250,
		'WIDTH':250
	}
}


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
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
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
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class EntryDetailView(DetailView):
	template_name='mlog/entrydetail.html'

	def get_object(self):
		current_entry=get_object_or_404(Entry,id=self.kwargs['pk'])

		if self.request.user.username:
			current_user=User.objects.get(username=self.request.user.username)
			ReadHistory.objects.create(user=current_user,entry=current_entry)
		else:
			ReadHistory.objects.create(entry=current_entry)

		return current_entry

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['like']=Like.objects.filter(entry=self.kwargs['pk']).count()
		context['comment']=Comment.objects.filter(entry=self.kwargs['pk']).count()
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		
		try:
			context['like_status']=Like.objects.filter(user__username=self.request.user.username,entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			context['like_status']=Like.objects.none()

		context['view_count']=ReadHistory.objects.filter(entry__id=self.kwargs['pk']).count()

		return context


class LikeProcess(LoginRequiredMixin,View):

	def post(self, *args, **kwargs):
		try:
			like_status=Like.objects.filter(user__username=self.request.user.username,entry=self.request.POST['pk'])
		except ObjectDoesNotExist:
			like_status=Like.objects.none()

		if like_status:
			like_status.delete()
		else:
			user=User.objects.get(username=self.request.user.username)
			entry=Entry.objects.get(id=self.request.POST['pk'])
			Like.objects.create(user=user,entry=entry)

		return redirect(self.request.META['HTTP_REFERER'])


class CommentListView(ListView):
	template_name='mlog/commentlist.html'

	def get_queryset(self):
		try:
			qs=Comment.objects.filter(id=self.kwargs['pk'])
		except ObjectDoesNotExist:
			qs=Comment.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['entry']=Entry.objects.get(id=self.kwargs['pk'])
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class LikeListView(ListView):
	template_name='mlog/likelist.html'

	def get_queryset(self):
		try:
			qs=Like.objects.filter(entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			qs=Like.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['entry']=Entry.objects.get(id=self.kwargs['pk'])
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class ArtistDetailView(DetailView):
	template_name='mlog/artistdetail.html'

	def get_object(self):
		current_artist=get_object_or_404(Artist,artist_name_id=self.kwargs['artist_name_id'])

		if self.request.user.username:
			current_user=User.objects.get(username=self.request.user.username)
			ArtistCheckedHistory.objects.create(user=current_user,artist=current_artist)

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


class CommentCreateView(LoginRequiredMixin,CreateView):
	form_class=CommentCreateForm
	template_name='mlog/commentcreate.html'

	def form_valid(self, form):
		form.instance.user_id=User.objects.get(username=self.request.user.username).id
		form.instance.entry_id=self.kwargs['pk']
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('mlog:commentlist',kwargs={'pk':self.kwargs['pk']})


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
	model=Song
	template_name='mlog/songdetail.html'
	


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


class FavoriteArtistProcess(LoginRequiredMixin,View):

	def post(self,*args,**kwargs):

		user=User.objects.get(username=self.request.user.username)
		artist=Artist.objects.get(artist_name_id=self.request.POST['artist_name_id'])

		try:
			fav_status=FavoriteArtist.objects.get(user=user,artist=artist)
		except ObjectDoesNotExist:
			fav_status=FavoriteArtist.objects.none()
		
		if fav_status:
			fav_status.delete()
		else:
			FavoriteArtist.objects.create(user=user,artist=artist)
		return redirect(self.request.META['HTTP_REFERER'])


class LikeEntryListView(ListView):
	template_name='mlog/userlikelist.html'

	def get_queryset(self):
		liked_entry=Like.objects.filter(user__username=self.kwargs['username']).values('entry__id')
		qs=Entry.objects.filter(id__in=liked_entry)
		return qs

	def get_context_data(self,**kwargs):
		context= super().get_context_data(**kwargs)
		context['detail_user']=User.objects.get(username=self.kwargs['username'])
		return context


class ArtistFavoriteUserListView(ListView):
	template_name='mlog/artistfavoriteuserlist.html'
	context_object_name='fav_users'

	def get_queryset(self):
		fav_user=FavoriteArtist.objects.filter(artist__artist_name_id=self.kwargs['artist_name_id']).values('user__id')
		qs=User.objects.filter(id__in=fav_user)
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['detail_artist']=Artist.objects.get(artist_name_id=self.kwargs['artist_name_id'])
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context