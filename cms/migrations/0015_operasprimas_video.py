# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 03:18
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_remove_productora_second_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='operasprimas',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
