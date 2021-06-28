from django.urls import path

from .views import FollowProcess, FollowingListView, FollowerListView

app_name='follow'
urlpatterns=[
	path('process/', FollowProcess.as_view(), name='process'),
	path('following/<str:username>/', FollowingListView.as_view(), name='following'),
	path('follower/<str:username>/', FollowerListView.as_view(), name='follower'),
]