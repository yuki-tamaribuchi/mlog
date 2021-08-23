from django.views.generic import ListView
from django.db.models import Q

from accounts.models import User
from musics.models import Song, Artist


class BaseSeachListView(ListView):
	template_name = 'search/list.html'

	def get_queryset(self):
		self.keyword = self.request.GET['keyword']
		qs = super().get_queryset()
		if not self.keyword:
			qs = self.model.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['keyword'] = self.request.GET['keyword']
		return context


class ArtistSearchListView(BaseSeachListView):
	model = Artist

	def get_queryset(self):
		qs = super().get_queryset()

		return qs.filter(
			Q(artist_name__icontains=self.keyword) | Q(slug__icontains=self.keyword)
		)
		


class SongSearchListView(BaseSeachListView):
	model = Song

	def get_queryset(self):
		qs = super().get_queryset()

		return qs.prefetch_related('artist').filter(
			Q(song_name__icontains = self.keyword)
		)


class UserSearchListView(BaseSeachListView):
	model = User

	def get_queryset(self):
		qs = super().get_queryset()

		return qs.filter(
			Q(username__icontains = self.keyword) | Q(handle__icontains = self.keyword)
		)