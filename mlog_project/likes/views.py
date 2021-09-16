from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from accounts.models import User
from entry.models import Entry
from notifications.tasks import add_notification

from .models import Like


def like_process(request):
	if request.method == 'GET':
		if not request.user.is_authenticated:
			login_url = '%s?next=%s'%(reverse('accounts:login'), reverse('entry:detail', kwargs={'pk':request.GET.get('entry_id')}))

			d = {
				'login_url':login_url
			}

			return JsonResponse(d)

	elif request.method == 'POST':
		try:
			like_instance = Like.objects.filter(user__username=request.user.username, entry=request.POST.get('entry_id'))
		except ObjectDoesNotExist:
			like_instance = Like.objects.none()

		if like_instance:
			like_instance.delete()
			like_status = False
		else:
			user = User.objects.get(username=request.user.username)
			entry = Entry.objects.get(id=request.POST.get('entry_id'))
			Like.objects.create(user=user, entry=entry)
			like_status = True
			

			add_notification.delay(
				user_from=request.user.username,
				user_to=entry.writer.username,
				notification_type='like',
			)

		like_count = Like.objects.filter(entry__id=request.POST.get('entry_id')).count()

		d = {
			'like_status':like_status,
			'like_count':like_count
		}
		
		

		return JsonResponse(d)


class EntryLikedUserListView(ListView):
	model = User
	template_name = 'likes/entry_liked_user_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		entry_liked_user_id_list = Like.objects.filter(entry=self.kwargs.get('pk'), user__is_active=True).values('user_id')
		try:
			return qs.filter(id__in=entry_liked_user_id_list)
		except ObjectDoesNotExist:
			return qs.none()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['entry'] = Entry.objects.get(id=self.kwargs['pk'], writer__is_active=True)
		return context


class UserLikedEntryListView(ListView):
	model = Entry
	template_name = 'likes/user_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		liked_entry = Like.objects.filter(user__username=self.kwargs['username'], entry__writer__is_active=True).values('entry__id')
		return qs.select_related('writer', 'song').filter(id__in=liked_entry)

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['detail_user'] = get_object_or_404(User, username=self.kwargs['username'], is_active=True)
		return context