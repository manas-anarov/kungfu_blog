
from django.urls import path

from django.conf.urls import include, url
from django.contrib.auth.views import login, logout;

from . import views

urlpatterns = [
	url(r'^login/$', login, {'template_name': 'myaccount/login.html'}, name='login'),
	url(r'^logout/$', logout, {'template_name': 'myaccount/logout.html'}, name='logout'),
	url(r'^register/$', views.register, name='register'),
]
