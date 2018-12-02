# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_userprofile_pgp_key_fingerprint'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='paper',
            index=models.Index(fields=['sort_date', 'legal_date'], name='mainapp_pap_sort_da_a4a03b_idx'),
        ),
    ]