# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0020_forumpost_fixed'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumblock',
            name='about',
            field=models.CharField(default='Тест', max_length=200, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
