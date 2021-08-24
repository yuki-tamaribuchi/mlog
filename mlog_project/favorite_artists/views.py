from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin


from accounts.models import User
from musics.models import Artist

from .models import FavoriteArtist


class FavoriteArtistProcess(LoginRequiredMixin,View):

	def post(self, *args, **kwargs):

		user = User.objects.get(username=self.request.user.username)
		artist = Artist.objects.get(slug=self.request.POST['slug'])

		try:
			fav_status = FavoriteArtist.objects.get(user=user, artist=artist)
		except ObjectDoesNotExist:
			fav_status = FavoriteArtist.objects.none()
		
		if fav_status:
			fav_status.delete()
		else:
			FavoriteArtist.objects.create(user=user, artist=artist)
		return redirect(self.request.META['HTTP_REFERER'])


class UserListByFavoritedArtistView(ListView):
	model = User
	template_name = 'favorite_artists/user_list_by_favorited_artist.html'
	context_object_name = 'fav_users'

	def get_queryset(self):
		qs = super().get_queryset()
		fav_user = FavoriteArtist.objects.filter(artist__slug=self.kwargs['slug']).values('user__id')
		return qs.filter(id__in=fav_user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['detail_artist'] = Artist.objects.get(slug=self.kwargs['slug'])
		return context


class UserFavoritesArtistListView(ListView):
	model = Artist
	template_name = 'favorite_artists/userfavoriteartistlist.html'

	def get_queryset(self):
		qs = super().get_queryset()
		fav_artist = FavoriteArtist.objects.filter(user__username=self.kwargs['username']).values('artist__id')
		return qs.filter(id__in=fav_artist)
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['detail_user'] = User.objects.get(username=self.kwargs['username'])
		return context