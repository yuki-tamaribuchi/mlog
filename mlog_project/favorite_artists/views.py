from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


from accounts.models import User
from musics.models import Artist

from .models import FavoriteArtist


def favorite_process(request):
	if request.method == 'GET':
		if not request.user.is_authenticated:
			login_url = '%s?next=%s'%(reverse('accounts:login'), reverse('musics:artist_detail', kwargs={'slug':request.GET.get('artist_slug')}))

			d = {
				'login_url':login_url
			}

			return JsonResponse(d)

	elif request.method == 'POST':
		user = User.objects.get(username=request.user.username)
		artist = Artist.objects.get(slug=request.POST.get('favorited_artist'))

		try:
			fav_instance = FavoriteArtist.objects.get(user=user, artist=artist)
		except ObjectDoesNotExist:
			fav_instance = FavoriteArtist.objects.none()
		
		if fav_instance:
			fav_instance.delete()
			fav_status = False
		else:
			FavoriteArtist.objects.create(user=user, artist=artist)
			fav_status = True
		
		d = {
			'fav_status':fav_status
		}

		return JsonResponse(d)


class UserListByFavoritedArtistView(ListView):
	model = User
	template_name = 'favorite_artists/user_list_by_favorited_artist.html'
	context_object_name = 'fav_users'

	def get_queryset(self):
		qs = super().get_queryset()
		fav_user = FavoriteArtist.objects.filter(artist__slug=self.kwargs['slug'], user__is_active=True).values('user__id')
		return qs.filter(id__in=fav_user).order_by('slug')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['detail_artist'] = Artist.objects.get(slug=self.kwargs['slug'])
		return context


class UserFavoritesArtistListView(ListView):
	model = Artist
	template_name = 'favorite_artists/user_favorites_artist_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		fav_artist = FavoriteArtist.objects.filter(user__username=self.kwargs['username']).values('artist__id')
		return qs.filter(id__in=fav_artist).order_by('slug')
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['detail_user'] = get_object_or_404(User, username=self.kwargs['username'], is_active=True)
		return context