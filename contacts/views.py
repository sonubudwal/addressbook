from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,CreateView,UpdateView

from django.core.urlresolvers import reverse

from contacts.models import Contact


class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    fields = '__all__'


class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context


class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})

        return context
