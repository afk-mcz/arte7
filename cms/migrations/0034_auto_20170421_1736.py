# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0033_cortometrajes_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cortometrajes',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
