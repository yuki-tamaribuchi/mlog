from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView as auth_login_view, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth import login

from entry.models import Entry
from likes.models import Like
from follow.models import Follow

from .forms import SignUpForm, UserUpdateForm, UserPasswordChangeForm, UserActiveStatusUpdateForm
from .models import User
from activity.tasks import user_checked_activity


class SignUpView(CreateView):
	form_class = SignUpForm
	template_name = 'accounts/signup.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('accounts:detail', username=self.request.user.username)
		return super().get(request, *args, **kwargs)

	def form_valid(self, form):
		to_return = super().form_valid(form)
		login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
		return to_return

	def get_success_url(self):
		return reverse('accounts:detail', kwargs={'username':self.object.username})

class LoginView(auth_login_view):
	template_name = 'accounts/login.html'
	redirect_authenticated_user = True

	def get_success_url(self):
		if self.request.GET.get('next'):
			return self.request.GET.get('next')
		return reverse('accounts:detail', kwargs={'username':self.request.user.username})


class UserDetailView(DetailView):
	context_object_name = 'detail_user'

	def get(self, request, *args, **kwargs):
		user_checked_activity.delay(self.kwargs['username'], request.user.username)
		return super().get(request, *args, **kwargs)

	def get_object(self):
		return get_object_or_404(User, username=self.kwargs['username'], is_active=True)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['entries'] = Entry.objects.select_related('writer', 'song').prefetch_related('song__artist').filter(writer__username=self.kwargs['username']).order_by('id').reverse()[:5]
		context['follow_count'] = Follow.objects.filter(user__username=self.kwargs['username'], follower__is_active=True).count()
		context['follower_count'] = Follow.objects.filter(follower__username=self.kwargs['username'], user__is_active=True).count()
		context['liked_entry_count'] = Like.objects.filter(user__username=self.kwargs['username'], entry__writer__is_active=True).count()

		if self.request.user.is_authenticated:
			user = get_object_or_404(User, username=self.request.user.username)	
			follow_user = get_object_or_404(User, username=self.kwargs['username'])
			context['is_myself'] = (user==follow_user)
			context['is_following'] = Follow.objects.filter(user__username=user.username, follower__username=follow_user.username).exists()
		
		return context


class UserUpdateView(LoginRequiredMixin,UpdateView):
	form_class = UserUpdateForm
	
	def get_object(self):
		return get_object_or_404(User, username=self.request.user.username)

	def get_success_url(self):
		return reverse('accounts:detail', kwargs={'username':self.request.user.username})


class UserEntryListView(ListView):
	model = Entry
	template_name = 'accounts/userentrylist.html'
	paginate_by = 20

	def get_queryset(self):
		qs = super().get_queryset()
		return qs.select_related('writer', 'song').prefetch_related('song__artist').filter(writer__username=self.kwargs['username'], writer__is_active=True).order_by('id').reverse()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['detail_user'] = get_object_or_404(User, username=self.kwargs.get('username'), is_active=True)
		return context


class UserPasswordChangeView(PasswordChangeView):
	template_name = 'accounts/passwordchange.html'
	form_class = UserPasswordChangeForm
	success_url = reverse_lazy('accounts:passwordchanged')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = 'accounts/passwordchangedone.html'


class UserPasswordResetView(PasswordResetView):
	template_name = 'accounts/password_reset.html'
	form_class = PasswordResetForm
	success_url = reverse_lazy('accounts:passwordresetdone')
	email_template_name = 'accounts/password_reset_email.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'
	

class UserPasswordResetConfirmView(PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'
	success_url = reverse_lazy('accounts:passwordresetcomplete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
	template_name = 'accounts/password_reset_complete.html'


class UserActiveStatusUpdateView(LoginRequiredMixin, UpdateView):
	form_class = UserActiveStatusUpdateForm
	template_name = 'accounts/active_status.html'

	def get_object(self):
		obj = User.objects.get(username=self.request.user.username)
		return obj
	
	def get_success_url(self):
		return reverse('mlog:top')