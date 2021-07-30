from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist

from entry.models import Entry
from accounts.models import User

from .models import Comment
from .forms import CommentForm


class CommentCreateView(LoginRequiredMixin, CreateView):
	form_class = CommentForm
	template_name = 'comments/comment_form.html'

	def form_valid(self, form):
		form.instance.user_id = User.objects.get(username=self.request.user.username).id
		form.instance.entry_id = self.kwargs['pk']
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('comments:list', kwargs={'pk':self.kwargs['pk']})


class CommentListView(ListView):
	model = Comment
	template_name = 'comments/list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		try:
			qs = qs.filter(entry_id=self.kwargs['pk'])
		except ObjectDoesNotExist:
			qs = qs.objects.none()
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['entry'] = Entry.objects.get(id=self.kwargs['pk'])
		return context




def get_comment_object(pk, username):
	obj = get_object_or_404(Comment, pk=pk, user__username=username)
	entry_pk = obj.entry.id
	return (obj, entry_pk)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
	form_class = CommentForm
	template_name = 'comments/comment_form.html'

	def get_object(self):
		obj, self.entry_pk = get_comment_object(self.kwargs['pk'], self.request.user.username)
		return obj

	def get_success_url(self):
		return reverse('comments:list', kwargs={'pk':self.entry_pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
	context_object_name = 'comment'
	template_name = 'comments/delete_confirm.html'

	def get_object(self):
		obj, self.entry_pk = get_comment_object(self.kwargs['pk'], self.request.user.username)
		return obj

	def get_success_url(self):
		return reverse('comments:list', kwargs={'pk':self.entry_pk})