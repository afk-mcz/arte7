# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 03:48
from __future__ import unicode_literals

import ckeditor.fields
import cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0021_auto_20170417_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(max_length=140)),
                ('slug', models.CharField(editable=False, max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Mensaje del home',
                'verbose_name_plural': 'Mensajes del home',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MosaicosHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.CharField(editable=False, max_length=200)),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('image', models.ImageField(upload_to=cms.models.upload_to)),
            ],
            options={
                'verbose_name': 'Mosaico del home',
                'verbose_name_plural': 'Mosaicos del home',
                'ordering': ['order'],
            },
        ),
    ]
