# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_auto_20171030_1024'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agendaitem',
            unique_together=set([]),
        ),
    ]