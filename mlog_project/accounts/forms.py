from django.forms import fields
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
	class Meta:
		model=User
		fields=('username','password1','password2','handle','biograph')