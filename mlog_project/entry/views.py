from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.shortcuts import get_object_or_404

from activity.models import EntryReadActivity
from accounts.models import User
from likes.models import Like
from comments.models import Comment

from .models import Entry
from .forms import EntryCreateForm

from activity.tasks import entry_read_activity


class EntryDetailView(DetailView):
	template_name = 'entry/detail.html'

	def get_object(self):
		current_entry = get_object_or_404(Entry,pk=self.kwargs['pk'])
		entry_read_activity.delay(self.kwargs['pk'], self.request.user.username)

		return current_entry


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['like_count'] = Like.objects.filter(entry=self.kwargs['pk']).count()
		context['comment_count'] = Comment.objects.filter(entry=self.kwargs['pk']).count()
		
		try:
			context['like_status'] = Like.objects.filter(user__username=self.request.user.username,entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			context['like_status'] = Like.objects.none()

		context['view_count'] = EntryReadActivity.objects.filter(entry__id=self.kwargs['pk']).count()

		return context


class EntryCreateView(LoginRequiredMixin,CreateView):
	form_class=EntryCreateForm
	template_name = 'entry/entry_form.html'

	def form_valid(self, form):
		form.instance.writer_id = User.objects.get(username=self.request.user.username).id
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('entry:detail',kwargs={'pk':self.object.id})


class EntryUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'entry/entry_form.html'
	fields = ('title','content','song')

	def get_object(self):
		return Entry.objects.get(writer__username=self.request.user.username,id=self.kwargs['pk'])


class EntryDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'entry/delete_confirm.html'

	def get_object(self):
		return Entry.objects.get(writer__username=self.request.user.username,id=self.kwargs['pk'])

	def get_success_url(self):
		return reverse('accounts:detail',kwargs={'username':self.request.user.username})