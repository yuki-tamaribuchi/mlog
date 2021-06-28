from django.urls import path

from .views import (
					RootRedirectView,
					SongCreateView, 
					TopView, 
					TimelineView, 
					EntryDetailView, 
					ArtistDetailView, 
					EntryCreateView, 
					SongCreateView, 
					ArtistCreateView, 
					SongDetailView, 
					EntryUpdateView, 
					EntryDeleteView, 
					PopupSongCreateView, 
					PopupArtistCreateView, 
					GenreCreateView, 
					PopupGenreCreateView, 
					FavoriteArtistProcess,
					ArtistFavoriteUserListView,
					GenreListView,
					ArtistByGenreListView,
				)

app_name='mlog'
urlpatterns=[
	path('', RootRedirectView.as_view(), name='rootredirect'),
	path('top/', TopView.as_view(), name='top'),
	path('timeline/', TimelineView.as_view(), name='timeline'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
	path('artist/<str:artist_name_id>/', ArtistDetailView.as_view(), name='artistdetail'),
	path('create/', EntryCreateView.as_view(), name='entrycreate'),
	path('create/song/', SongCreateView.as_view(), name='songcreate'),
	path('create/artist/', ArtistCreateView.as_view(), name='artistcreate'),
	path('song/<int:pk>/', SongDetailView.as_view(), name='songdetail'),
	path('update/entry/<int:pk>/', EntryUpdateView.as_view(), name='entryupdate'),
	path('delete/entry/<int:pk>/', EntryDeleteView.as_view(), name='entrydelete'),
	path('popup/song_create/', PopupSongCreateView.as_view(), name='popupsongcreate'),
	path('popup/artist_create', PopupArtistCreateView.as_view(), name='popupartistcreate'),
	path('create/genre/', GenreCreateView.as_view(), name='genrecreate'),
	path('popup/genre_create',PopupGenreCreateView.as_view(),name='popupgenrecreate'),
	path('favprocess/', FavoriteArtistProcess.as_view(), name='favprocess'),
	path('artist/<str:artist_name_id>/favoriteuser/', ArtistFavoriteUserListView.as_view(), name='favoriteuser'),
	path('genre/', GenreListView.as_view(), name='genre_list'),
	path('genre/<str:genre_name>/artist/', ArtistByGenreListView.as_view(), name='artist_by_genre'),
]