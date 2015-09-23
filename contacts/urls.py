__author__ = 'fateh'

from django.conf.urls import url
import contacts.views

from . import views

urlpatterns = [
   url(r'^$', contacts.views.ListContactView.as_view(),name='contacts-list',),
   url(r'^new/$', contacts.views.CreateContactView.as_view(),name='contacts-new',),
]