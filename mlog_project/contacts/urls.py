from django.urls import path

from contacts.views import CreateContactThreadAndConentView, ContactThreadDetailView, ContactContentUpdateView

app_name = 'contacts'

urlpatterns = [
	path('create/', CreateContactThreadAndConentView.as_view(), name='create'),
	path('detail/<int:pk>/', ContactThreadDetailView.as_view(), name='detail'),
	path('update/<int:pk>/', ContactContentUpdateView.as_view(), name='update'),
]