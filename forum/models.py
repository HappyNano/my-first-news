# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ForumBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
		

class ForumSubBlock(models.Model):
    block = models.ForeignKey(ForumBlock, related_name='subblock')
    title = models.CharField(max_length=200, verbose_name='Название')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    block = models.ForeignKey(ForumSubBlock, related_name='post')
    title = models.CharField(max_length=200, verbose_name='Название')
    body = models.TextField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    active = models.BooleanField(default=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments')
    user = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)
		