from django.urls import path

from .views import TopView, TimelineView, EntryDetailView, LikeProcess, CommentListView

app_name='mlog'
urlpatterns=[
	path('top/', TopView.as_view(), name='top'),
	path('timeline/', TimelineView.as_view(), name='timeline'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
	path('likeprocess/', LikeProcess.as_view(), name='likeprocess'),
	path('detail/<int:pk>/comment/', CommentListView.as_view(), name='commentlist'),
]