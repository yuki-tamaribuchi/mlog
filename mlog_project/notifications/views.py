from django.shortcuts import redirect
from django.views.generic import ListView

from notifications.tasks import notification_read
from notifications.models import Notifications

def notification_redirect(request, pk, username):
	if request.method=='GET':
		notification_read.delay(pk)
		return redirect('accounts:detail', username=username)


class NotificationListView(ListView):
	model = Notifications
	template_name = 'notifications/list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		return qs.filter(
			user_to=self.request.user,
		)