from django.forms import ModelForm, fields

from .models import Comment


class CommentCreateForm(ModelForm):
	class Meta:
		model=Comment
		fields=('comment',)