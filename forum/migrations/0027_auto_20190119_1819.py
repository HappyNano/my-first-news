# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-19 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0026_auto_20190119_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
    ]
