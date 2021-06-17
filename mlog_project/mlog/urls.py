from django.urls import path

from .views import TopView

app_name='mlog'
urlpatterns=[
	path('top/', TopView.as_view(), name='top'),
]