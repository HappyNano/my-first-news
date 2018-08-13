# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('news.urls')),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^account/', include('userprofile.urls')),
]