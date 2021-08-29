#https://stackoverflow.com/questions/15889794/creating-one-django-form-to-save-two-models

from django.db.models import fields
from django.forms import ModelForm
from django.forms.models import model_to_dict, fields_for_model

from contacts.models import ContactThreads, ContactContent

class ContactThreadAndContentForm(ModelForm):

	def __init__(self, instance=None, *args, **kwargs):
		_fields = ('content',)
		super(ContactThreadAndContentForm, self).__init__(*args, **kwargs)
		self.fields.update(fields_for_model(ContactContent, _fields))
	
	class Meta:
		model = ContactThreads
		fields = ('category',)