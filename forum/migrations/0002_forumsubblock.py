# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumSubBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.ForumBlock')),
            ],
        ),
    ]