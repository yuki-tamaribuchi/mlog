from django.db.models import Count

from notifications.models import Notifications

def unread_notifications(request):
	unread_notifications_list = Notifications.objects.select_related(
		'user_from',
		'user_to',
	).filter(
		user_to__username=request.user.username,
		is_read = 0
	).order_by(
		'recieved_datetime'
	)[:10]

	unread_notifications_count = unread_notifications_list.count()

	return {
		'unread_notifications_list':unread_notifications_list,
		'unread_notifications_count':unread_notifications_count,
	}