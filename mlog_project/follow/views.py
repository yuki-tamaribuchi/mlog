from django.http.response import JsonResponse
from django.shortcuts import redirect, resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import User
from notifications.tasks import add_notification

from .models import Follow


def follow_process(request):

	if request.method == 'POST':
		user = User.objects.get(username=request.user.username)
		follower_user = User.objects.get(username=request.POST.get('follower_user'))
		follow_instance = Follow.objects.filter(user__username=user.username, follower__username=follower_user.username)
		
		if follow_instance.exists():
			follow_instance.delete()
			follow_status = False
		else:
			Follow.objects.create(user=user, follower=follower_user)
			follow_status = True

			add_notification.delay(
				user_from=request.user.username,
				user_to=follower_user.username,
				notification_type='follow',
			)

		
		follower_count = Follow.objects.filter(follower__username=request.POST.get('follower_user')).count()

		d = {
			'follow_status':follow_status,
			'follower_count':follower_count,
		}
		return JsonResponse(d)
		


class BaseListView(ListView):
	template_name = 'follow/list.html'
	model = Follow

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		this_page_user = User.objects.get(username=self.kwargs['username'])
		context['this_page_username'] = this_page_user.username
		context['this_page_handle'] = this_page_user.handle
		return context



class FollowingListView(BaseListView):
	context_object_name = 'follows'

	def get_queryset(self):
		qs = super().get_queryset()
		try:
			return qs.select_related('follower', 'user').filter(user__username=self.kwargs['username'])
		except ObjectDoesNotExist:
			return qs.none()


class FollowerListView(BaseListView):
	context_object_name = 'followers'

	def get_queryset(self):
		qs = super().get_queryset()
		try:
			return qs.select_related('follower', 'user').filter(follower__username=self.kwargs['username'])
		except ObjectDoesNotExist:
			return qs.none()