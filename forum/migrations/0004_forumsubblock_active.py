# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20181103_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumsubblock',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
