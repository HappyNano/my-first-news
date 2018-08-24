# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^profile/avatar/add$', views.update_avatar, name='avatar_add'),
	url(r'^profile/change_password/$', views.change_password, name='change_password'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$',  views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
	url(r'^ajax/get_avatar/$', views.get_avatar, name='get_avatar'),
	url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

urlpatterns += [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)