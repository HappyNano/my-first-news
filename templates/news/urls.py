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
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
	url(r'^change_password/$', views.change_password, name='change_password'),
]

urlpatterns += [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]