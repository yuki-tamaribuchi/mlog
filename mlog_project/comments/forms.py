from django.db.models import fields
from django.forms import ModelForm

from .models import Comment


class CommentCreateForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('comment',)

class CommentUpdateForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('comment',)