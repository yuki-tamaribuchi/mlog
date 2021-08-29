from django.urls import path

from contacts.views import CreateContactThreadAndConentView

app_name = 'contacts'

urlpatterns = [
	path('create/', CreateContactThreadAndConentView.as_view(), name='create'),
]