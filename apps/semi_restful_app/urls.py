from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(?P<id>\d+)/show$', views.show),
    url(r'^new/$',views.new),
    url(r'^new/process$',views.process),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/edit/edit_process$', views.edit_process),
    url(r'^(?P<id>\d+)/destroy$', views.destroy)


]

