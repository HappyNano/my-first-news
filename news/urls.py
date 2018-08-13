# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^about/$', views.about, name='about'), 
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
	url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]