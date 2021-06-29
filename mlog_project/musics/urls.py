from django.urls import path

from .views import (
	ArtistDetailView,
	SongDetailView,
	ArtistCreateView,
	SongCreateView,
	PopupArtistCreateView,
	PopupSongCreateView,
	PopupGenreCreateView,
	GenreCreateView,
	GenreListView,
	ArtistByGenreListView,
)


app_name='musics'

urlpatterns=[
	path('detail/artist/<str:artist_name_id>/', ArtistDetailView.as_view(), name='artist_detail'),
	path('detail/song/<int:pk>/', SongDetailView.as_view(), name='song_detail'),

	path('create/song/', SongCreateView.as_view(), name='song_create'),
	path('create/artist/', ArtistCreateView.as_view(), name='artist_create'),
	path('create/genre/', GenreCreateView.as_view(), name='genre_create'),

	path('create/song/popup/', PopupSongCreateView.as_view(), name='song_create_popup'),
	path('create/artist/popup/', PopupArtistCreateView.as_view(), name='artist_create_popup'),
	path('create/genre/popup/', PopupGenreCreateView.as_view(), name='genre_create_popup'),

	path('list/genre/', GenreListView.as_view(), name='genre_list'),
	path('list/genre/<str:genre_name>/artist/', ArtistByGenreListView.as_view(), name='artist_by_genre'),
]