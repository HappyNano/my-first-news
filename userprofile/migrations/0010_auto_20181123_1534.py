# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_auto_20181120_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AddField(
            model_name='profile',
            name='last_online',
            field=models.DateTimeField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
