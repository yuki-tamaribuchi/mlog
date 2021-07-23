from allauth.account.utils import perform_login
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import ObjectDoesNotExist

from .models import User

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
	def pre_social_login(self, request, sociallogin):
		user = sociallogin.user
		
		if user.id:
			return
		try:
			exist_user = User.objects.get(email=user.email)
			sociallogin.state['process'] = 'connect'
			perform_login(request, exist_user, 'none')
		except ObjectDoesNotExist:
			pass