from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry, Like, Comment
from accounts.models import User, Follow


class TopView(ListView):
	model=Entry
	template_name='mlog/topview.html'

	def get_queryset(self):
		try:
			qs=Entry.objects.all().order_by('-id')
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs


class TimelineView(LoginRequiredMixin, ListView):
	model=Entry
	template_name='mlog/timeline.html'

	def get_queryset(self):
		follows=Follow.objects.filter(user__username=self.request.user.username).values('follower__username')
		
		try:
			qs=Entry.objects.filter(writer__username__in=follows)
			print(qs)
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs


class EntryDetailView(DetailView):
	template_name='mlog/entrydetail.html'

	def get_object(self):
		return get_object_or_404(Entry,id=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['like']=Like.objects.filter(entry=self.kwargs['pk']).count()
		context['comment']=Comment.objects.filter(entry=self.kwargs['pk']).count()
		
		try:
			context['like_status']=Like.objects.filter(user__username=self.request.user.username,entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			context['like_status']=Like.objects.none()

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
		return context