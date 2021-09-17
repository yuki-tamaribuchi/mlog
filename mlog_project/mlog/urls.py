from django.urls import path

from .views import (
					RootRedirectView,
					TopView, 
					TimelineView, 
					login_with_sample_user,
				)

app_name='mlog'
urlpatterns=[
	path('', RootRedirectView.as_view(), name='rootredirect'),
	path('top/', TopView.as_view(), name='top'),
	path('timeline/', TimelineView.as_view(), name='timeline'),
	path('login_with_sample_user/', login_with_sample_user, name='login_with_sample_user'),
]