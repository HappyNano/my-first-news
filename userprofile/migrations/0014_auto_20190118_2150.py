# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_auto_20190118_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('ban', 'ban this user'), ('change.your', 'change your profile'), ('rep', 'rep user'))},
        ),
    ]