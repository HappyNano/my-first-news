# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-16 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0019_auto_20181209_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='fixed',
            field=models.BooleanField(default=False),
        ),
    ]
