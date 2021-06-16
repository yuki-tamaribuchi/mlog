from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignUpView, LoginView, UserDetailView, UserUpdateView, FollowProcess, FollowListView

app_name='accounts'
urlpatterns=[
	path('signup/',SignUpView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(template_name='accounts/loggedout.html'), name='logout'),
	path('detail/<str:username>/', UserDetailView.as_view(), name='detail'),
	path('update/', UserUpdateView.as_view(), name='update'),
	path('follow/', FollowProcess.as_view(), name='follow'),
	path('follow/<str:username>/', FollowListView.as_view(), name='followlist'),
]