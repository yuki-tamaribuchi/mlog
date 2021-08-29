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


class ContactThreadDetailView(LoginRequiredMixin, UserPassesTestMixin, FormMixin, DetailView):
	model = ContactThreads
	form_class = ContactContentForm
	template_name = 'contacts/detail.html'
	

	def test_func(self):
		object = self.get_object()
		return object.user == self.request.user or self.request.user.is_staff

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['contact_content_list'] = ContactContent.objects.filter(
			parent_thread__id=self.object.id
		).order_by(
			'datetime'
		)

		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_vaild(form)
		else:
			return self.form_invalid(form)

	def form_vaild(self, form):
		form.instance.user = self.request.user
		form.instance.parent_thread = self.object
		form.save()
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse('contacts:detail', kwargs={'pk':self.object.id})


class ContactContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ContactContent
	form_class = ContactContentForm
	template_name = 'contacts/content_form.html'

	def test_func(self):
		object = self.get_object()
		return object.user == self.request.user

	def get_success_url(self):
		return reverse('contacts:detail', kwargs={'pk':self.object.parent_thread.id})


class ContactThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = ContactThreads
	template_name = 'contacts/delete_confirm.html'

	def test_func(self) :
		object = self.get_object()
		return object.user == self.request.user or self.request.user.is_staff

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['first_content'] = ContactContent.objects.filter(
			parent_thread__id=self.kwargs.get('pk')
			).select_related(
				'user',
			).order_by(
				'datetime'
			)[0]
		
		return context
	
	def get_success_url(self):
		return reverse('contacts:create')
