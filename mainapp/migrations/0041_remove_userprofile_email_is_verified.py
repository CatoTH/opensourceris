# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_auto_20171104_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email_is_verified',
        ),
    ]