from mlog_project.celery import app

from accounts.models import User

from notifications.models import Notifications

@app.task()
def add_notification(user_from, user_to, notification_type):

	user_from_obj = User.objects.get(username=user_from)
	user_to_obj = User.objects.get(username=user_to)

	content_prefix = '%s(%s)さんが'%(user_from_obj.handle, user_from_obj.username)

	if notification_type=='like':
		content_suffix = '記事にいいねしました。'
	elif notification_type=='follow':
		content_suffix = 'あなたをフォローしました。'

	Notifications.objects.create(
		user_from=user_from_obj,
		user_to=user_to_obj,
		content=content_prefix+content_suffix,
	)


@app.task()
def notification_read(pk):
	notification_obj = Notifications.objects.get(pk=pk)
	notification_obj.is_read = 1
	notification_obj.save()
