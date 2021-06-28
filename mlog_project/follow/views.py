from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User

from .models import Follow



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

class FollowProcess(LoginRequiredMixin,View):

	def post(self,*args,**kwargs):
		user=User.objects.get(username=self.request.user.username)	
		follow_user=User.objects.get(username=self.request.POST['username'])
		following=Follow.objects.filter(user__username=user.username,follower__username=follow_user.username)

		if user==follow_user:
			return redirect(self.request.META['HTTP_REFERER'])
		
		if following.exists():
			following.delete()
		else:
			Follow.objects.create(user=user,follower=follow_user)

		return redirect(self.request.META['HTTP_REFERER'])


class FollowingListView(ListView):
	model=Follow
	template_name='follow/following.html'
	context_object_name='follows'

	def get_queryset(self):
		try:
			qs=Follow.objects.filter(user__username=self.kwargs['username'])
		except ObjectDoesNotExist:
			qs=Follow.objects.none()
		return qs
	
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		this_page_user=User.objects.get(username=self.kwargs['username'])
		context['this_page_username']=this_page_user.username
		context['this_page_handle']=this_page_user.handle
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class FollowerListView(ListView):
	model=Follow
	template_name='follow/follower.html'
	context_object_name='followers'

	def get_queryset(self):
		try:
			qs=Follow.objects.filter(follower__username=self.kwargs['username'])
		except ObjectDoesNotExist:
			qs=Follow.objects.none()
		return qs
	
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		this_page_user=User.objects.get(username=self.kwargs['username'])
		context['this_page_username']=this_page_user.username
		context['this_page_handle']=this_page_user.handle
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context