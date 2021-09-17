from django.db import models

from accounts.models import User

class Notifications(models.Model):

	user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_send_user')
	user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_recieve_user')
	content =models.CharField(max_length=100)
	is_read = models.BooleanField(default=0)
	recieved_datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'From:%s, To:%s, is-Read:%d'%(self.user_from.username, self.user_to.username, self.is_read)