from django.urls import path

from .views import FollowingListView, FollowerListView, follow_process

app_name='follow'
urlpatterns=[
	path('follow/', follow_process, name='follow'),
	path('following/<str:username>/', FollowingListView.as_view(), name='following'),
	path('follower/<str:username>/', FollowerListView.as_view(), name='follower'),
]