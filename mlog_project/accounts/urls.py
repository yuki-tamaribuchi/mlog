from django.urls import path

from .views import SignUpView, LoginView, UserDetailView

app_name='accounts'
urlpatterns=[
	path('signup/',SignUpView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('detail/<str:username>/', UserDetailView.as_view(), name='detail')
]