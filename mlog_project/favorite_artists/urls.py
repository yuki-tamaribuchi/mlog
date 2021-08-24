from django.urls import path

from .views import FavoriteArtistProcess, UserListByFavoritedArtistView, UserFavoriteArtistListView

app_name='favorite_artists'
urlpatterns=[
	path('process/', FavoriteArtistProcess.as_view(), name='process'),
	path('artist/<str:slug>/', UserListByFavoritedArtistView.as_view(), name='userfavorite'),
	path('user/<str:username>/', UserFavoriteArtistListView.as_view(), name='favoriteartist'),
]