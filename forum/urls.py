# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.forum, name='forum'),
	url(r'^block/(?P<pk>\d+)/$', views.block, name='block'),
	url(r'^check/', views.checking, name='check'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='forum_post_detail'),
	url(r'^post/add/(?P<pk>\d+)/$', views.post_add, name='forum_post_add'),
	url(r'^ajax/post_freeze$', views.close, name='post_freeze'),
	url(r'^ajax/post_check$', views.check, name='post_check'),
	url(r'^ajax/post_delete$', views.delete, name='post_delete'),
]