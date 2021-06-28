from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin


from accounts.models import User
from mlog.models import Artist

from .models import FavoriteArtist


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


class FavoriteArtistProcess(LoginRequiredMixin,View):

	def post(self,*args,**kwargs):

		user=User.objects.get(username=self.request.user.username)
		artist=Artist.objects.get(artist_name_id=self.request.POST['artist_name_id'])

		try:
			fav_status=FavoriteArtist.objects.get(user=user,artist=artist)
		except ObjectDoesNotExist:
			fav_status=FavoriteArtist.objects.none()
		
		if fav_status:
			fav_status.delete()
		else:
			FavoriteArtist.objects.create(user=user,artist=artist)
		return redirect(self.request.META['HTTP_REFERER'])


class ArtistFavoriteUserListView(ListView):
	template_name='favorite_artists/artistfavoriteuserlist.html'
	context_object_name='fav_users'

	def get_queryset(self):
		fav_user=FavoriteArtist.objects.filter(artist__artist_name_id=self.kwargs['artist_name_id']).values('user__id')
		qs=User.objects.filter(id__in=fav_user)
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['detail_artist']=Artist.objects.get(artist_name_id=self.kwargs['artist_name_id'])
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class UserFavoriteArtistListView(ListView):
	template_name='favorite_artists/userfavoriteartistlist.html'

	def get_queryset(self):
		fav_artist=FavoriteArtist.objects.filter(user__username=self.kwargs['username']).values('artist__id')
		qs=Artist.objects.filter(id__in=fav_artist)
		return qs
	
	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['detail_user']=User.objects.get(username=self.kwargs['username'])
		return context