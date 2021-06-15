from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView as auth_login_view

from .forms import SignUpForm


class SignUpView(CreateView):
	form_class=SignUpForm
	template_name='accounts/signup.html'
	success_url='/'


class LoginView(auth_login_view):
	template_name='accounts/login.html'
