from django.urls import path

from .views import (
	EntryDetailView,
	EntryCreateView,
	EntryUpdateView,
	EntryDeleteView,
)

app_name='entry'

urlpatterns=[
	path('create/', EntryCreateView.as_view(), name='create'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
	path('update/<int:pk>/', EntryUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', EntryDeleteView.as_view(), name='delete'),
]