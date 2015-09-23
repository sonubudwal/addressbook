from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import CreateView
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