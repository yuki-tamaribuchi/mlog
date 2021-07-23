from django.urls import path

from .views import (
	CommentCreateView,
	CommentListView,
	CommentUpdateView,
)

app_name='comments'
urlpatterns=[
	path('create/<int:pk>/', CommentCreateView.as_view(), name='create'),
	path('list/<int:pk>/', CommentListView.as_view(), name='list'),
	path('update/<int:pk>/', CommentUpdateView.as_view(), name='update'),
]