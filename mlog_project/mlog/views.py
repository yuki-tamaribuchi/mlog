from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from entry.models import Entry
from follow.models import Follow


class RootRedirectView(View):
	def get(self,request):
		if request.user.username:
			return redirect('mlog:timeline')
		else:
			return redirect('mlog:top')


class TopView(ListView):
	model = Entry
	template_name = 'mlog/topview.html'
	paginate_by = 20

	def get_queryset(self):
		qs = super().get_queryset()
		try:
			return qs.select_related('writer', 'song').prefetch_related('song__artist').all().order_by('-id')
		except ObjectDoesNotExist:
			return qs.none()


class TimelineView(LoginRequiredMixin, ListView):
	model = Entry
	template_name = 'mlog/timeline.html'
	paginate_by = 20

	def get_queryset(self):
		qs = super().get_queryset()
		follows = Follow.objects.filter(user__username=self.request.user.username).values('follower__username')
		try:
			return qs.select_related('song' ,'writer').prefetch_related('song__artist').filter(writer__username__in=follows).order_by('-id')
		except ObjectDoesNotExist:
			return qs.none()