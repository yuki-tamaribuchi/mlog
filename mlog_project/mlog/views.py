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

from .models import Entry
from .forms import EntryCreateForm
from accounts.models import User
from comments.models import Comment
from likes.models import Like
from follow.models import Follow
from activity.models import EntryReadActivity
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


class EntryCreateView(LoginRequiredMixin,CreateView):
	form_class=EntryCreateForm
	template_name='mlog/entrycreate.html'

	def form_valid(self, form):
		form.instance.writer_id=User.objects.get(username=self.request.user.username).id
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('mlog:detail',kwargs={'pk':self.object.id})


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