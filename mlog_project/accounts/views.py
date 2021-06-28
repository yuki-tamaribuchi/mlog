from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView as auth_login_view, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Q

from .forms import SignUpForm, UserUpdateForm, UserPasswordChangeForm
from .models import User, Follow
from mlog.models import Entry, Artist
from likes.models import Like


PROFILE_IMAGE_SIZE={
	'SM':{
		'HEIGHT':100,
		'WIDTH':100
	},
	'MID':{
		'HEIGHT':250,
		'WIDTH':250
	}
}



class SignUpView(CreateView):
	form_class=SignUpForm
	template_name='accounts/signup.html'

	def get_success_url(self):
		return reverse_lazy('accounts:detail',kwargs={'username':self.object.username})

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
		context['entries']=Entry.objects.filter(writer__username=self.kwargs['username']).order_by('id').reverse()[:5]
		context['follow_count']=Follow.objects.filter(user__username=self.kwargs['username']).count()
		context['follower_count']=Follow.objects.filter(follower__username=self.kwargs['username']).count()
		context['profile_image_size']=PROFILE_IMAGE_SIZE['MID']
		context['liked_entry_count']=Like.objects.filter(user__username=self.kwargs['username']).count()

		if self.request.user.username:
			user=get_object_or_404(User, username=self.request.user.username)	
			follow_user=get_object_or_404(User, username=self.kwargs['username'])
			context['is_myself']=(user==follow_user)
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
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class FollowerListView(ListView):
	model=Follow
	template_name='accounts/followerlist.html'
	context_object_name='followers'

	def get_queryset(self):
		try:
			qs=Follow.objects.filter(follower__username=self.kwargs['username'])
		except ObjectDoesNotExist:
			qs=Follow.objects.none()
		return qs
	
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		this_page_user=get_object_or_404(User,username=self.kwargs['username'])
		context['this_page_username']=this_page_user.username
		context['this_page_handle']=this_page_user.handle
		context['profile_image_size']=PROFILE_IMAGE_SIZE['SM']
		return context


class UserEntryListView(ListView):
	model=Entry
	template_name='mlog/userentrylist.html'
	paginate_by=20

	def get_queryset(self):
		qs=Entry.objects.filter(writer__username=self.kwargs['username']).order_by('id').reverse()
		return qs

	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['detail_user']=User.objects.get(username=self.kwargs['username'])
		return context


class UserPasswordChangeView(PasswordChangeView):
	template_name='accounts/passwordchange.html'
	form_class=UserPasswordChangeForm
	success_url=reverse_lazy('accounts:passwordchanged')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
	template_name='accounts/passwordchangedone.html'


class UserPasswordResetView(PasswordResetView):
	template_name='accounts/password_reset.html'
	form_class=PasswordResetForm
	success_url=reverse_lazy('accounts:passwordresetdone')
	email_template_name='accounts/password_reset_email.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
	template_name='accounts/password_reset_done.html'
	

class UserPasswordResetConfirmView(PasswordResetConfirmView):
	template_name='accounts/password_reset_confirm.html'
	success_url=reverse_lazy('accounts:passwordresetcomplete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
	template_name='accounts/password_reset_complete.html'