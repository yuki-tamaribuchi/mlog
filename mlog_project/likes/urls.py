from django.urls import path

from .views import LikeProcess, EntrysLikeListView, UsersLikeListView

app_name='likes'
urlpatterns=[
	path('process/', LikeProcess.as_view(), name='process'),
	path('userlist/<str:username>/', UsersLikeListView.as_view(), name='user_list'),
	path('entrylist/<int:pk>/', EntrysLikeListView.as_view(), name='entry_list'),
]