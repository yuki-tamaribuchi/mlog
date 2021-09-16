from django.urls import path

from .views import EntryLikedUserListView, UserLikedEntryListView, like_process

app_name='likes'
urlpatterns=[
	path('like/', like_process, name='like'),
	path('userlist/<str:username>/', UserLikedEntryListView.as_view(), name='user_list'),
	path('entrylist/<int:pk>/', EntryLikedUserListView.as_view(), name='entry_list'),
]