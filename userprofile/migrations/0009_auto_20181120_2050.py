# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20180822_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('post.close', 'post close'),)},
        ),
    ]