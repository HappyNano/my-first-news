# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ForumBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    small = models.CharField(max_length=200, verbose_name='Мелкий текст')
    about = models.CharField(max_length=200, verbose_name='Описание')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
		

class ForumSubBlock(models.Model):
    block = models.ForeignKey(ForumBlock, related_name='subblock')
    title = models.CharField(max_length=200, verbose_name='Название')
    about = models.CharField(max_length=200, verbose_name='Описание')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    block = models.ForeignKey(ForumSubBlock, related_name='post')
    title = models.CharField(max_length=30, verbose_name='Название')
    body = models.TextField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now,
            blank=True, null=True)
    active = models.BooleanField(default=True,blank=True)
    views = models.TextField(verbose_name="list of views")
    fixed = models.BooleanField(default=False)
    checked = models.BooleanField(default=False,blank=True)

    class Meta:
        permissions = (
			('forum.post.add.your', 'add your post'),
			('forum.post.delete.foreign', 'delete foreign post'),
			('forum.post.change.foreign', 'change foreign post'),
			('forum.post.close', 'close post'),
        )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def author_rep(self):
        user = User.objects.get(username=self.author)
        text = user.profile.rep()
        return '%s' % (text)

    def get_user_online(self):
        user = User.objects.get(username=self.author)
        text = user.profile.get_online()
        return '%s' % (text)

    def get_user_online_short(self):
        user = User.objects.get(username=self.author)
        text = user.profile.get_online_short()
        return '%s' % (text)

    def get_user_avatar(self):
        user = User.objects.get(username=self.author)
        text = user.profile.avatar.url
        return '%s' % (text)

    def __str__(self):
        return self.title
		

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments')
    user = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    checked = models.BooleanField(default=False,blank=True)

    class Meta:
        permissions = (
			('forum.comment.add.your', 'add your comment'),
			('forum.comment.delete.foreign', 'delete foreign comment'),
			('forum.comment.change.foreign', 'change foreign comment.'),
        )

    def author_rep(self):
        user = User.objects.get(username=self.user)
        text = user.profile.rep()
        return '%s' % (text)

    def get_user_online(self):
        user = User.objects.get(username=self.user)
        text = user.profile.get_online()
        return '%s' % (text)

    def get_user_online_short(self):
        user = User.objects.get(username=self.user)
        text = user.profile.get_online_short()
        return '%s' % (text)

    def get_user_avatar(self):
        user = User.objects.get(username=self.user)
        text = user.profile.avatar.url
        return '%s' % (text)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)
		