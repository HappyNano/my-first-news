# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
 
 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='images/users/', null=True, blank=True, verbose_name='Аватар', default='images/users/PaperTest.jpg')
 
    def __unicode__(self):
        return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'