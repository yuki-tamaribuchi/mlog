from activity import models
from mlog_project.celery import app

from accounts.models import User
from entry.models import Entry

@app.task()
def entry_read_activity(pk, username):
	current_entry = Entry.objects.get(pk=pk)

	if username:
		current_user = User.objects.get(username=username)
		models.EntryReadActivity.objects.create(
			entry=current_entry,
			user=current_user
		)
	else:
		models.EntryReadActivity.objects.create(
			entry=current_entry
		)


