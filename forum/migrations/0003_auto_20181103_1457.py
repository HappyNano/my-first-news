# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_forumsubblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumsubblock',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SubBlock', to='forum.ForumBlock'),
        ),
    ]