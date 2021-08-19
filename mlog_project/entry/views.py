from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.shortcuts import get_object_or_404

from activity.models import EntryReadActivity
from accounts.models import User
from likes.models import Like
from comments.models import Comment
from musics.models import Song

from .models import Entry
from .forms import EntryForm

from activity.tasks import entry_read_activity


class EntryCreateView(LoginRequiredMixin,CreateView):
	form_class = EntryForm
	template_name = 'entry/entry_form.html'

	def form_valid(self, form):
		form.instance.writer_id = User.objects.get(username=self.request.user.username).id
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('entry:detail', kwargs={'pk':self.object.id})


class EntryDetailView(DetailView):
	template_name = 'entry/detail.html'

	def get_object(self):
		current_entry = get_object_or_404(Entry, pk=self.kwargs.get('pk'))
		entry_read_activity.delay(self.kwargs.get('pk'), self.request.user.username)

		return current_entry


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['like_count'] = Like.objects.filter(entry=self.kwargs.get('pk')).count()
		context['comment_count'] = Comment.objects.filter(entry=self.kwargs.get('pk')).count()
		
		try:
			context['like_status'] = Like.objects.filter(user__username=self.request.user.username, entry=self.kwargs.get('pk'))
		except ObjectDoesNotExist:
			context['like_status'] = Like.objects.none()

		context['view_count'] = EntryReadActivity.objects.filter(entry__id=self.kwargs.get('pk')).count()

		return context


class EntryUpdateView(LoginRequiredMixin, UpdateView):
	form_class = EntryForm
	template_name = 'entry/entry_form.html'

	def get_object(self):
		return Entry.objects.get(writer__username=self.request.user.username, id=self.kwargs.get('pk'))


class EntryDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'entry/delete_confirm.html'

	def get_object(self):
		return Entry.objects.get(writer__username=self.request.user.username, id=self.kwargs.get('pk'))

	def get_success_url(self):
		return reverse('accounts:detail', kwargs={'username':self.request.user.username})


class EntryListBySongView(ListView):
	model = Entry
	template_name = 'entry/entry_list_by_song.html'
	paginate_by = 15

	def get_queryset(self):
		qs = super().get_queryset()

		try:
			return qs.filter(song__id=self.kwargs.get('pk'))
		except ObjectDoesNotExist:
			return qs.none()

	def get_context_data(self, *args, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['song'] = get_object_or_404(Song, id=self.kwargs.get('pk'))
		return context