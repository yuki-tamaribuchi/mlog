from django.urls import path

from .views import SongCreateView, TopView, TimelineView, EntryDetailView, LikeProcess, CommentListView, LikeListView, ArtistDetailView, EntryCreateView, CommentCreateView, SongCreateView, ArtistCreateView, SongDetailView, EntryUpdateView, EntryDeleteView, PopupSongCreateView, PopupArtistCreateView, GenreCreateView, PopupGenreCreateView, ArtistSearchListView, SongSearchListView

app_name='mlog'
urlpatterns=[
	path('top/', TopView.as_view(), name='top'),
	path('timeline/', TimelineView.as_view(), name='timeline'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
	path('likeprocess/', LikeProcess.as_view(), name='likeprocess'),
	path('detail/<int:pk>/comment/', CommentListView.as_view(), name='commentlist'),
	path('detail/<int:pk>/like/', LikeListView.as_view(), name='likelist'),
	path('artist/<str:artist_name_id>/', ArtistDetailView.as_view(), name='artistdetail'),
	path('create/', EntryCreateView.as_view(), name='entrycreate'),
	path('commentcreate/<int:pk>/', CommentCreateView.as_view(), name='commentcreate'),
	path('create/song/', SongCreateView.as_view(), name='songcreate'),
	path('create/artist/', ArtistCreateView.as_view(), name='artistcreate'),
	path('song/<int:pk>/', SongDetailView.as_view(), name='songdetail'),
	path('update/entry/<int:pk>/', EntryUpdateView.as_view(), name='entryupdate'),
	path('delete/entry/<int:pk>/', EntryDeleteView.as_view(), name='entrydelete'),
	path('popup/song_create/', PopupSongCreateView.as_view(), name='popupsongcreate'),
	path('popup/artist_create', PopupArtistCreateView.as_view(), name='popupartistcreate'),
	path('create/genre/', GenreCreateView.as_view(), name='genrecreate'),
	path('popup/genre_create',PopupGenreCreateView.as_view(),name='popupgenrecreate'),
	path('search/artist', ArtistSearchListView.as_view(), name='artistsearch'),
	path('search/song', SongSearchListView.as_view(), name='songsearch'),
]