from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.views import LogoutView

from accounts import views
from accounts.models import User

class TestAuthUrls(TestCase):

	def test_signup(self):
		view = resolve('/accounts/signup/')
		self.assertEqual(view.func.view_class, views.SignUpView)

	def test_login(self):
		view = resolve('/accounts/login/')
		self.assertEqual(view.func.view_class, views.LoginView)

	def test_logout(self):
		view = resolve('/accounts/logout/')
		self.assertEqual(view.func.view_class, LogoutView)

	def test_password_change(self):
		view = resolve('/accounts/password/')
		self.assertEqual(view.func.view_class, views.UserPasswordChangeView)

	def test_password_change_done(self):
		view = resolve('/accounts/password/changed/')
		self.assertEqual(view.func.view_class, views.UserPasswordChangeDoneView)

	def test_password_reset(self):
		view = resolve('/accounts/password/reset/')
		self.assertEqual(view.func.view_class, views.UserPasswordResetView)

	def test_password_reset_done(self):
		view = resolve('/accounts/password/reset/done/')
		self.assertEqual(view.func.view_class, views.UserPasswordResetDoneView)

	'''
	def test_password_reset_confirm(self):
		view = resolve('/accounts/password/confirm/')
	'''

	def test_password_reset_complete(self):
		view = resolve('/accounts/password/reset/complete/')
		self.assertEqual(view.func.view_class, views.UserPasswordResetCompleteView)


class TestUserAccountUrls(TestCase):
	@classmethod
	def setUpTestData(cls):
		User.objects.create(
			username='testuser',
			handle='testhandle',
			biograph='testbiograph',
			profile_image='test.jpg'
		)

	
	def test_detail(self):
		user_instance = User.objects.first()
		username = user_instance.username
		view = resolve('/accounts/detail/%s/'%(username))
		self.assertEqual(view.func.view_class, views.UserDetailView)

	def test_detail_entry(self):
		user_instance = User.objects.first()
		username = user_instance.username
		view = resolve('/accounts/detail/%s/entry/'%(username))
		self.assertEqual(view.func.view_class, views.UserEntryListView)

	def test_update(self):
		view = resolve('/accounts/update/')
		self.assertEqual(view.func.view_class, views.UserUpdateView)
		