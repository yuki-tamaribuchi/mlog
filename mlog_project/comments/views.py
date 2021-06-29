from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.core.exceptions import ObjectDoesNotExist

from entry.models import Entry
from accounts.models import User
from utils.utils import get_profile_image_size

from .models import Comment
from .forms import CommentCreateForm


class CommentCreateView(LoginRequiredMixin,CreateView):
	form_class=CommentCreateForm
	template_name='comments/create.html'

	def form_valid(self, form):
		form.instance.user_id=User.objects.get(username=self.request.user.username).id
		form.instance.entry_id=self.kwargs['pk']
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('comments:list',kwargs={'pk':self.kwargs['pk']})


class CommentListView(ListView):
	template_name='comments/list.html'

	def get_queryset(self):
		try:
			qs=Comment.objects.filter(id=self.kwargs['pk'])
		except ObjectDoesNotExist:
			qs=Comment.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['entry']=Entry.objects.get(id=self.kwargs['pk'])
		context['profile_image_size']=get_profile_image_size('SM')
		return context