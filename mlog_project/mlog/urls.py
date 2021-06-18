from django.urls import path

from .views import SongCreateView, TopView, TimelineView, EntryDetailView, LikeProcess, CommentListView, LikeListView, ArtistDetailView, EntryCreateView, CommentCreateView, SongCreateView, ArtistCreateView, SongDetailView

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
]