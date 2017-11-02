from django.conf.urls import patterns, url
from rolodex import views

urlpatterns = [
               # Default view if the user have not navigated yet
               url(r'^$', views.index, name='index'),
               
               # company related urls
               url(r'^company/add/$', views.company_add, name='company_add'),
               url(r'^company/edit/(?P<company_name>[A-Za-z0-9. \-]+)/$', views.company_edit, name='company_edit'),
               url(r'^company/list/$', views.company_list, name='company_list'),
               url(r'^company/delete/(?P<company_name>[A-Za-z0-9.\- ]+)/$', views.company_delete, name='company_delete'),
               
               # company related urls
               url(r'^contact/add/$', views.contact_add, name='contact_add'),
               url(r'^contact/add/(?P<company_name>[A-Za-z0-9.\- ]+)/$', views.contact_add, name='contact_add'),
               url(r'^contact/edit/(?P<contact_id>[0-9]+)/$', views.contact_edit, name='contact_edit'),
               url(r'^contact/list/$', views.contact_list, name='contact_list'),
               url(r'^contact/list/(?P<company_name>[A-Za-z0-9.\- ]+)/$', views.contact_list, name='contact_list'),
               url(r'^contact/delete/(?P<contact_id>[0-9]+)/$', views.contact_delete, name='contact_delete'),
               
               url(r'^docs/notes/$', views.doc_notes, name='doc_notes'),
               
               ]


