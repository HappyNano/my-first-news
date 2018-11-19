# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import ForumBlock,ForumSubBlock,ForumPost

admin.site.register(ForumBlock)
admin.site.register(ForumSubBlock)
admin.site.register(ForumPost)
