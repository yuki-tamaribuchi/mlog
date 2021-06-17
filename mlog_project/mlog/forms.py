from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Entry


class EntryCreateForm(ModelForm):
	class Meta:
		model=Entry
		fields=('title','content','song')