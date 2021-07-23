from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User

from .models import Follow


class FollowProcess(LoginRequiredMixin,View):

	def post(self,*args,**kwargs):
		user = User.objects.get(username=self.request.user.username)	
		follow_user = User.objects.get(username=self.request.POST['username'])
		following = Follow.objects.filter(user__username=user.username,follower__username=follow_user.username)

		if user==follow_user:
			return redirect(self.request.META['HTTP_REFERER'])
		
		if following.exists():
			following.delete()
		else:
			Follow.objects.create(user=user,follower=follow_user)

		return redirect(self.request.META['HTTP_REFERER'])


class BaseListView(ListView):
	model = Follow

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		this_page_user = User.objects.get(username = self.kwargs['username'])
		context['this_page_username'] = this_page_user.username
		context['this_page_handle'] = this_page_user.handle
		return context



class FollowingListView(BaseListView):
	template_name = 'follow/following.html'
	context_object_name = 'follows'

	def get_queryset(self):
		qs = super().get_queryset()
		try:
			return qs.filter(user__username = self.kwargs['username'])
		except ObjectDoesNotExist:
			return qs.none()


class FollowerListView(BaseListView):
	template_name = 'follow/follower.html'
	context_object_name = 'followers'

	def get_queryset(self):
		qs = super().get_queryset()
		try:
			return qs.filter(follower__username = self.kwargs['username'])
		except ObjectDoesNotExist:
			return qs.none()