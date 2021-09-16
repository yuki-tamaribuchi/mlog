from django.http.response import Http404, HttpResponseNotAllowed
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.shortcuts import get_object_or_404

from activity.models import EntryReadActivity
from accounts.models import User
from likes.models import Like
from comments.models import Comment
from musics.models import Artist, Song

from .models import Entry
from .forms import EntryForm

from activity.tasks import entry_read_activity


class EntryCreateView(LoginRequiredMixin,CreateView):
	form_class = EntryForm
	template_name = 'entry/entry_form.html'

	def form_valid(self, form):
		form.instance.writer = User.objects.get(username=self.request.user.username)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('entry:detail', kwargs={'pk':self.object.id})


class EntryDetailView(DetailView):
	model = Entry
	template_name = 'entry/detail.html'

	def get(self, request, *args, **kwargs):
		entry_read_activity.delay(self.kwargs.get('pk'), request.user.username)
		return super().get(request, *args, **kwargs)

	def get_object(self):
		obj = super().get_object()
		if obj.writer.is_active:
			return obj
		else:
			raise Http404

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['like_count'] = Like.objects.filter(entry=self.kwargs.get('pk'), user__is_active=True).count()
		context['comment_count'] = Comment.objects.filter(entry=self.kwargs.get('pk'), author__is_active=True).count()
		
		try:
			context['like_status'] = Like.objects.get(user__username=self.request.user.username, entry=self.kwargs.get('pk'))
		except ObjectDoesNotExist:
			context['like_status'] = Like.objects.none()

		context['view_count'] = EntryReadActivity.objects.filter(entry__id=self.kwargs.get('pk')).count()

		return context


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Entry
	form_class = EntryForm
	template_name = 'entry/entry_form.html'

	def test_func(self):
		object = self.get_object()
		return object.writer.id == self.request.user.id

	def get_success_url(self):
		return reverse('entry:detail', kwargs={'pk':self.object.id})


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Entry
	template_name = 'entry/delete_confirm.html'

	def test_func(self):
		object = self.get_object()
		return object.writer.id == self.request.user.id

	def get_success_url(self):
		return reverse('accounts:detail', kwargs={'username':self.request.user.username})


class EntryListBySongView(ListView):
	model = Entry
	template_name = 'entry/entry_list.html'
	paginate_by = 12

	def get_queryset(self):
		qs = super().get_queryset()

		try:
			return qs.select_related('writer', 'song').prefetch_related('song__artist').filter(song__id=self.kwargs.get('pk'), writer__is_active=True)
		except ObjectDoesNotExist:
			return qs.none()

	def get_context_data(self, *args, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['song'] = get_object_or_404(Song, id=self.kwargs.get('pk'))
		return context


class EntryListByArtistView(ListView):
	model = Entry
	template_name = 'entry/entry_list.html'
	paginate_by = 12

	def get_queryset(self):
		qs = super().get_queryset()

		try:
			return qs.select_related(
				'writer', 'song'
			).prefetch_related(
				'song__artist'
			).filter(
				song__artist__slug=self.kwargs.get('slug'),
				writer__is_active=True,
			).order_by('id')
		except ObjectDoesNotExist:
			return qs.none()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['artist'] = get_object_or_404(Artist, slug=self.kwargs.get('slug'))
		return context