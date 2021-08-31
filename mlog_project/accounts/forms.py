from django.forms.models import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

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


class UserActiveStatusUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ('is_active',)