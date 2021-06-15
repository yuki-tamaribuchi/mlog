from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView as auth_login_view
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm, UserUpdateForm
from .models import User


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

	def get_object(self):
		return get_object_or_404(User,username=self.kwargs['username'])


class UserUpdateView(LoginRequiredMixin,UpdateView):
	model=User
	template_name='accounts/userupdate.html'
	form_class=UserUpdateForm
	
	def get_object(self):
		return get_object_or_404(User,username=self.request.user.username)
