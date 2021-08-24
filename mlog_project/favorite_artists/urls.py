from django.urls import path

from .views import FavoriteArtistProcess, UserListByFavoritedArtistView, UserFavoriteArtistListView

app_name='favorite_artists'
urlpatterns=[
	path('process/', FavoriteArtistProcess.as_view(), name='process'),
	path('artist/<str:slug>/', UserListByFavoritedArtistView.as_view(), name='user_list_by_favorited_artist'),
	path('user/<str:username>/', UserFavoriteArtistListView.as_view(), name='favoriteartist'),
]