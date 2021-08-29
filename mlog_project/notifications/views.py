from django.shortcuts import redirect

from notifications.tasks import notification_read

def notification_redirect(request, pk, username):
	if request.method=='GET':
		notification_read.delay(pk)
		return redirect('accounts:detail', username=username)