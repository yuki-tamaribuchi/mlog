from django.urls import path

from .views import FavoriteArtistProcess, UserListByFavoritedArtistView, UserFavoritesArtistListView, favorite_process

app_name='favorite_artists'
urlpatterns=[
	path('favorite/', favorite_process, name='favorite'),
	path('process/', FavoriteArtistProcess.as_view(), name='process'),
	path('artist/<str:slug>/', UserListByFavoritedArtistView.as_view(), name='user_list_by_favorited_artist'),
	path('user/<str:username>/', UserFavoritesArtistListView.as_view(), name='user_favorites_artist_list'),
]