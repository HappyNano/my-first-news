# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.forum, name='forum'),
	url(r'^block/(?P<pk>\d+)/$', views.block, name='block'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]