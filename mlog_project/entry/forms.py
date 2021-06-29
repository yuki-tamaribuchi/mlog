from django.forms import ModelForm

from .models import Entry


class EntryCreateForm(ModelForm):
	class Meta:
		model=Entry
		fields=('title','content','song')