from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignUpView, LoginView, UserDetailView

app_name='accounts'
urlpatterns=[
	path('signup/',SignUpView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('detail/<str:username>/', UserDetailView.as_view(), name='detail')
]