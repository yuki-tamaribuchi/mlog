from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView as auth_login_view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .forms import SignUpForm, UserUpdateForm
from .models import User, Follow
from mlog.models import Entry


class SignUpView(CreateView):
	form_class=SignUpForm
	template_name='accounts/signup.html'
	success_url='/'


class LoginView(auth_login_view):
	template_name='accounts/login.html'
	redirect_authenticated_user=True

	def get_success_url(self):
		return reverse_lazy('accounts:detail',kwargs={'username':self.request.user.username})


class UserDetailView(DetailView):
	model=User
	template_name='accounts/userdetail.html'
	context_object_name='detail_user'

	def get_object(self):
		return get_object_or_404(User,username=self.kwargs['username'])

	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['entries']=Entry.objects.filter(writer__username=self.kwargs['username']).order_by('-id')
		context['follow_count']=Follow.objects.filter(user__username=self.kwargs['username']).count()
		context['follower_count']=Follow.objects.filter(follower__username=self.kwargs['username']).count()

		user=get_object_or_404(User, username=self.request.user.username)	
		follow_user=get_object_or_404(User, username=self.kwargs['username'])
		context['is_myself']=(user==follow_user)
		print(context['is_myself'])
		context['is_following']=Follow.objects.filter(user__username=user.username,follower__username=follow_user.username).exists()
		
		return context


class UserUpdateView(LoginRequiredMixin,UpdateView):
	model=User
	template_name='accounts/userupdate.html'
	form_class=UserUpdateForm
	
	def get_object(self):
		return get_object_or_404(User,username=self.request.user.username)

	def get_success_url(self):
		return reverse_lazy('accounts:detail',kwargs={'username':self.request.user.username})

class FollowProcess(LoginRequiredMixin,View):

	def post(self,*args,**kwargs):
		user=get_object_or_404(User, username=self.request.user.username)	
		follow_user=get_object_or_404(User, username=self.request.POST['username'])
		following=Follow.objects.filter(user__username=user.username,follower__username=follow_user.username)

		if user==follow_user:
			return redirect(self.request.META['HTTP_REFERER'])
		
		if following.exists():
			following.delete()
		else:
			Follow.objects.create(user=user,follower=follow_user)

		return redirect(self.request.META['HTTP_REFERER'])


class FollowListView(ListView):
	model=Follow
	template_name='accounts/followlist.html'
	context_object_name='follows'

	def get_queryset(self):
		try:
			qs=Follow.objects.filter(user__username=self.kwargs['username'])
			#queryset=get_object_or_404(Follow,user__username=self.kwargs['username'])
			print(qs)
		except ObjectDoesNotExist:
			qs=Follow.objects.none()
		return qs
	
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		this_page_user=get_object_or_404(User,username=self.kwargs['username'])
		context['this_page_username']=this_page_user.username
		context['this_page_handle']=this_page_user.handle
		return context