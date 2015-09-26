__author__ = 'fateh'

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import contacts.views

from . import views

urlpatterns = [
   url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list',),
   url(r'^new/$', contacts.views.CreateContactView.as_view(), name='contacts-new',),
   url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit',),
]
urlpatterns += staticfiles_urlpatterns()