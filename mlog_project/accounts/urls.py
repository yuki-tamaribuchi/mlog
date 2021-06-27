from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (SignUpView, 
					LoginView, 
					UserDetailView, 
					UserUpdateView, 
					FollowProcess, 
					FollowListView, 
					FollowerListView,
					UserSearchListView,
					UserFavoriteArtistListView,
					UserEntryListView,
					UserPasswordChangeView,
					UserPasswordChangeDoneView,
)

app_name='accounts'
urlpatterns=[
	path('signup/',SignUpView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(template_name='accounts/loggedout.html'), name='logout'),
	path('detail/<str:username>/', UserDetailView.as_view(), name='detail'),
	path('update/', UserUpdateView.as_view(), name='update'),
	path('follow/', FollowProcess.as_view(), name='follow'),
	path('follow/<str:username>/', FollowListView.as_view(), name='followlist'),
	path('follower/<str:username>/', FollowerListView.as_view(), name='followerlist'),
	path('search', UserSearchListView.as_view(), name='usersearch'),
	path('detail/<str:username>/favoriteartist/', UserFavoriteArtistListView.as_view(), name='favoriteartist'),
	path('detail/<str:username>/entry/', UserEntryListView.as_view(), name='userentrylist'),
	path('password/change/', UserPasswordChangeView.as_view(), name='passwordchange'),
	path('password/changed/', UserPasswordChangeDoneView.as_view(), name='passwordchanged')
]