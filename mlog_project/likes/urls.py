from django.urls import path

from .views import EntryLikedUserListView, UserLikedEntryListView, like_process

app_name='likes'
urlpatterns=[
	path('like/', like_process, name='like'),
	path('entrylist/<int:pk>/', EntryLikedUserListView.as_view(), name='entry_liked_user_list'),
	path('user_liked_entry_list/<str:username>/', UserLikedEntryListView.as_view(), name='user_liked_entry_list'),
]