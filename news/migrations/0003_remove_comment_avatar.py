# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-13 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comment_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='avatar',
        ),
    ]
