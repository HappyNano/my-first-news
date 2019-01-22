# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from userprofile.models import Profile

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    text_short = models.TextField(verbose_name='Короткий текст')
    text_full = models.TextField(verbose_name='Полный текст')
    image = models.ImageField(upload_to='images/post/', null=True, blank=True, verbose_name='Изображение')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Small_post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    text_full = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
	

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_user_online(self):
        user = User.objects.get(username=self.user)
        text = user.profile.get_online()
        return '%s' % (text)

    def get_user_avatar(self):
        user = User.objects.get(username=self.user)
        text = user.profile.avatar.url
        return '%s' % (text)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)
		
