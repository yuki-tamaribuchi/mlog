from django.urls import path

from .views import FavoriteArtistProcess, ArtistFavoriteUserListView, UserFavoriteArtistListView

app_name='favorite_artists'
urlpatterns=[
	path('process/', FavoriteArtistProcess.as_view(), name='process'),
	path('artist/<str:artist_name_id>/', ArtistFavoriteUserListView.as_view(), name='userfavorite'),
	path('user/<str:username>/',UserFavoriteArtistListView.as_view(), name='favoriteartist'),
]