from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.db.transaction import atomic

from contacts.models import ContactThreads, ContactContent
from contacts.forms import ContactThreadAndContentForm, ContactContentForm


class CreateContactThreadAndConentView(LoginRequiredMixin, CreateView):
	form_class = ContactThreadAndContentForm
	template_name = 'contacts/contact_thread_form.html'

	def get_queryset(self):
		return super().get_queryset()

	def form_valid(self, form):
		form.instance.user_id = self.request.user.id

		try:
			with atomic():
				form.save()
				contact_content = ContactContent(
					parent_thread=form.instance,
					user=self.request.user,
					content = form.cleaned_data['content']
				)
				contact_content.save()
				return super().form_valid(form)
		except:
			return super().form_invalid(form)


	def get_success_url(self):
		return reverse('contacts:detail', kwargs={'pk':self.object.id})
