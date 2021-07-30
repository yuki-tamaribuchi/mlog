from django.db.models import fields
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('comment',)