from django.urls import path

from .views import(
	ArtistSearchListView,
	SongSearchListView,
	UserSearchListView,
)

app_name='search'
urlpatterns=[
	path('artist/', ArtistSearchListView.as_view(), name='artist'),
	path('song/', SongSearchListView.as_view(), name='song'),
	path('user/', UserSearchListView.as_view(), name='user'),
]