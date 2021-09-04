from django.urls import path

from notifications.views import notification_redirect, NotificationListView

app_name='notifications'

urlpatterns = [
	path('redirect/<int:pk>/<str:username>/', notification_redirect, name='redirect'),
	path('list/', NotificationListView.as_view(), name='list'),
]