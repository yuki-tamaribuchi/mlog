from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

from utils.utils import get_profile_image_size
from activity.models import EntryReadActivity
from accounts.models import User
from likes.models import Like
from comments.models import Comment

from .models import Entry
from .forms import EntryCreateForm

class EntryDetailView(DetailView):
	template_name='entry/detail.html'

	def get_object(self):
		current_entry=Entry.objects.get(pk=self.kwargs['pk'])

		if self.request.user.username:
			current_user=User.objects.get(username=self.request.user.username)
			if not current_entry.writer.username == current_user.username:
				EntryReadActivity.objects.create(user=current_user,entry=current_entry)
		else:
			EntryReadActivity.objects.create(entry=current_entry)

		return current_entry

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['like_count']=Like.objects.filter(entry=self.kwargs['pk']).count()
		context['comment_count']=Comment.objects.filter(entry=self.kwargs['pk']).count()
		context['profile_image_size']=get_profile_image_size('XS')
		
		try:
			context['like_status']=Like.objects.filter(user__username=self.request.user.username,entry=self.kwargs['pk'])
		except ObjectDoesNotExist:
			context['like_status']=Like.objects.none()

		context['view_count']=EntryReadActivity.objects.filter(entry__id=self.kwargs['pk']).count()

		return context


class EntryCreateView(LoginRequiredMixin,CreateView):
	form_class=EntryCreateForm
	template_name='entry/create.html'

	def form_valid(self, form):
		form.instance.writer_id=User.objects.get(username=self.request.user.username).id
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('entry:detail',kwargs={'pk':self.object.id})


class EntryUpdateView(LoginRequiredMixin, UpdateView):
	template_name='entry/update.html'
	fields=('title','content','song')

	def get_object(self):
		return Entry.objects.get(writer__username=self.request.user.username,id=self.kwargs['pk'])


class EntryDeleteView(LoginRequiredMixin, DeleteView):
	template_name='entry/delete_confirm.html'

	def get_object(self):
		return Entry.objects.get(writer__username=self.request.user.username,id=self.kwargs['pk'])

	def get_success_url(self):
		return reverse_lazy('accounts:detail',kwargs={'username':self.request.user.username})