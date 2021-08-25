from django.urls import path

from .views import EntrysLikeListView, UsersLikeListView, like_process

app_name='likes'
urlpatterns=[
	path('like/', like_process, name='like'),
	path('userlist/<str:username>/', UsersLikeListView.as_view(), name='user_list'),
	path('entrylist/<int:pk>/', EntrysLikeListView.as_view(), name='entry_list'),
]