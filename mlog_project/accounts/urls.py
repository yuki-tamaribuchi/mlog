from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (SignUpView, 
					LoginView, 
					UserDetailView, 
					UserUpdateView, 
					UserEntryListView,
					UserPasswordChangeView,
					UserPasswordChangeDoneView,
					UserPasswordResetView,
					UserPasswordResetDoneView,
					UserPasswordResetConfirmView,
					UserPasswordResetCompleteView,
					UserActiveStatusUpdateView,
)

app_name = 'accounts'
urlpatterns = [
	path('signup/',SignUpView.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(template_name='accounts/loggedout.html'), name='logout'),

	path('password/', UserPasswordChangeView.as_view(), name='password'),
	path('password/changed/', UserPasswordChangeDoneView.as_view(), name='passwordchanged'),
	path('password/reset/', UserPasswordResetView.as_view(), name='passwordreset'),
	path('password/reset/done/', UserPasswordResetDoneView.as_view(), name='passwordresetdone'),
	path('password/reset/confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='passwordresetconfirm'),
	path('password/reset/complete/', UserPasswordResetCompleteView.as_view(), name='passwordresetcomplete'),
	
	path('detail/<str:username>/', UserDetailView.as_view(), name='detail'),
	path('detail/<str:username>/entry/', UserEntryListView.as_view(), name='userentrylist'),
	path('update/', UserUpdateView.as_view(), name='update'),
	path('update/active_status/', UserActiveStatusUpdateView.as_view(), name='active_status'),
]