from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth import login

from accounts.models import User
from entry.models import Entry
from follow.models import Follow
from favorite_artists.models import FavoriteArtist


def login_as_sample_user(request):
	if request.method=='GET':
		sample_user = User.objects.get(username='sampleuser')
		login(request, sample_user)
		return redirect('mlog:top')


class RootRedirectView(View):
	def get(self,request):
		if request.user.is_authenticated:
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
			return qs.select_related('writer', 'song').prefetch_related('song__artist').filter(writer__is_active=True).order_by('created_at').reverse()
		except ObjectDoesNotExist:
			return qs.none()


class TimelineView(LoginRequiredMixin, ListView):
	model = Entry
	template_name = 'mlog/timeline.html'
	paginate_by = 20

	def get_queryset(self):
		qs = super().get_queryset()
		follows = Follow.objects.filter(user__username=self.request.user.username, follower__is_active=True).values('follower__username')
		favorite_artists = FavoriteArtist.objects.filter(user__username=self.request.user.username).values('artist__slug')
		try:
			return qs.select_related(
				'song' ,'writer'
			).prefetch_related(
				'song__artist'
			).filter(
				Q(writer__username__in=follows) | Q(song__artist__slug__in=favorite_artists)
			).exclude(
				writer__username=self.request.user.username
			).order_by(
				'created_at'
			).reverse().distinct()

		except ObjectDoesNotExist:
			return qs.none()