from django.forms import fields
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm, PasswordChangeForm

from allauth.account.forms import LoginForm as allauth_login_form

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'handle', 'biograph', 'profile_image')


class UserUpdateForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('handle', 'biograph', 'profile_image')


class UserPasswordChangeForm(PasswordChangeForm):
	class Meta:
		model = User
		fields = '__all__'