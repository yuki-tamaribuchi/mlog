from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User
from entry.models import Entry
from utils.utils import get_profile_image_size

from .models import Like


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


class EntrysLikeListView(ListView):
	template_name='likes/entry_list.html'

	def get_queryset(self):
		try:
			qs=Like.objects.filter(entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			qs=Like.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['entry']=Entry.objects.get(id=self.kwargs['pk'])
		context['profile_image_size']=get_profile_image_size('SM')
		return context


class UsersLikeListView(ListView):
	template_name='likes/user_list.html'

	def get_queryset(self):
		liked_entry=Like.objects.filter(user__username=self.kwargs['username']).values('entry__id')
		qs=Entry.objects.filter(id__in=liked_entry)
		return qs

	def get_context_data(self,**kwargs):
		context= super().get_context_data(**kwargs)
		context['detail_user']=User.objects.get(username=self.kwargs['username'])
		return context