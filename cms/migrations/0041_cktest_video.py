# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 22:22
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0040_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='cktest',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=1),
            preserve_default=False,
        ),
    ]
