# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-08 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20180708_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password1',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='password2',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
