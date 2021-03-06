from django.urls import path

from contacts.views import CreateContactThreadAndContentView, ContactThreadDetailView, ContactContentUpdateView, ContactThreadDeleteView, ContactListView

app_name = 'contacts'

urlpatterns = [
	path('create/', CreateContactThreadAndContentView.as_view(), name='create'),
	path('detail/<int:pk>/', ContactThreadDetailView.as_view(), name='detail'),
	path('update/<int:pk>/', ContactContentUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', ContactThreadDeleteView.as_view(), name='delete'),
	path('list/', ContactListView.as_view(), name='list'),
]