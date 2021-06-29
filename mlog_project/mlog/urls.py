from django.urls import path

from .views import (
					RootRedirectView,
					TopView, 
					TimelineView, 
					EntryDetailView, 
					EntryCreateView, 
					EntryUpdateView, 
					EntryDeleteView, 
				)

app_name='mlog'
urlpatterns=[
	path('', RootRedirectView.as_view(), name='rootredirect'),
	path('top/', TopView.as_view(), name='top'),
	path('timeline/', TimelineView.as_view(), name='timeline'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
	path('create/', EntryCreateView.as_view(), name='entrycreate'),
	path('update/entry/<int:pk>/', EntryUpdateView.as_view(), name='entryupdate'),
	path('delete/entry/<int:pk>/', EntryDeleteView.as_view(), name='entrydelete'),
]