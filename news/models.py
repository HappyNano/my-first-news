# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


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


from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email_confirmed = models.BooleanField(default=False)
    first_name = models.TextField(max_length=50, blank=True)
    last_name = models.TextField(max_length=50, blank=True)
    password1 = models.TextField(max_length=50, blank=True)
    password2 = models.TextField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='images/users/', null=True, blank=True, verbose_name='Аватар')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
	

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
		
