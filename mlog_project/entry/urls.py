from django.urls import path, include

from .views import (
	EntryDetailView,
	EntryCreateView,
	EntryUpdateView,
	EntryDeleteView,
	EntryListBySongView,
)

app_name='entry'

urlpatterns=[
	path('create/', EntryCreateView.as_view(), name='create'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
	path('update/<int:pk>/', EntryUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', EntryDeleteView.as_view(), name='delete'),

	path('list/song/<int:pk>/', EntryListBySongView.as_view(), name='entry_list_by_song'),

	path('select2/', include('django_select2.urls')),
]