from django.urls import path

from .views import FollowProcess, FollowingListView, FollowerListView, follow_process

app_name='follow'
urlpatterns=[
	path('follow/', follow_process, name='follow'),
	path('process/', FollowProcess.as_view(), name='process'),
	path('following/<str:username>/', FollowingListView.as_view(), name='following'),
	path('follower/<str:username>/', FollowerListView.as_view(), name='follower'),
]