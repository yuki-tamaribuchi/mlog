from django.urls import path, include

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
	ArtistUpdateView,
	SongUpdateView,
	SongByArtistListView,
	search_spotify_tracks,
	select_spotify_tracks,
)


app_name='musics'

urlpatterns=[
	path('detail/artist/<slug:slug>/', ArtistDetailView.as_view(), name='artist_detail'),
	path('detail/song/<int:pk>/', SongDetailView.as_view(), name='song_detail'),

	path('create/song/', SongCreateView.as_view(), name='song_create'),
	path('create/artist/', ArtistCreateView.as_view(), name='artist_create'),
	path('create/genre/', GenreCreateView.as_view(), name='genre_create'),

	path('create/song/popup/', PopupSongCreateView.as_view(), name='song_create_popup'),
	path('create/artist/popup/', PopupArtistCreateView.as_view(), name='artist_create_popup'),
	path('create/genre/popup/', PopupGenreCreateView.as_view(), name='genre_create_popup'),

	path('update/artist/<str:slug>/', ArtistUpdateView.as_view(), name='artist_update'),
	path('update/song/<int:pk>/', SongUpdateView.as_view(), name='song_update'),

	path('list/genre/', GenreListView.as_view(), name='genre_list'),
	path('list/genre/<str:genre_name>/artist/', ArtistByGenreListView.as_view(), name='artist_by_genre'),
	path('list/artist/<str:slug>/song/', SongByArtistListView.as_view(), name='song_by_artist'),

	path('search_spotify_tracks/', search_spotify_tracks, name='search_spotify_tracks'),
	path('select_spotify_tracks/', select_spotify_tracks, name='select_spotify_tracks'),

	path('select2/', include('django_select2.urls')),
]