# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
import pytz

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", default='avatars/Zapadno-sibirskaya-layka-na-gazone-lodozo.com_-600x476.png')
    skype = models.CharField(max_length=50, blank=True)
    vk = models.CharField(max_length=50, blank=True)
    discord = models.CharField(max_length=50, blank=True)
    last_online = models.DateTimeField(auto_now_add=True, blank=True)
    rep_plus = models.TextField(verbose_name="list of rep_plus")
    rep_minus = models.TextField(verbose_name="list of rep_minus")

    class Meta:
        permissions = (
            ('profile.ban', 'ban this user'),
			('profile.rep', 'rep user'),
        )

    def rep(self):
        return '%s' % (len(self.rep_plus.split(" ")) - len(self.rep_minus.split(" ")))
		
    def get_online(self):
        timezone.activate(pytz.timezone("Europe/Moscow"))
        dt = timezone.now()
        if (dt - self.last_online).seconds < 120:
            text = "online"
        else:
            text = self.last_online.strftime("%d %B %H:%M")
        return '%s' % (text)
		
    def get_online_short(self):
        timezone.activate(pytz.timezone("Europe/Moscow"))
        dt = timezone.now()
        if (dt - self.last_online).seconds < 120:
            text = "online"
        else:
            text = "offline"
        return '%s' % (text)

    def get_user_avatar(self):
        return '%s' % (self.avatar.url)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
	
