from django.urls import path

from .views import TopView, TimelineView, EntryDetailView

app_name='mlog'
urlpatterns=[
	path('top/', TopView.as_view(), name='top'),
	path('timeline/', TimelineView.as_view(), name='timeline'),
	path('detail/<int:pk>/', EntryDetailView.as_view(), name='detail'),
]