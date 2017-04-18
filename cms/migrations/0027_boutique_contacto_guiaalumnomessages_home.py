# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 05:43
from __future__ import unicode_literals

import ckeditor.fields
import cms.models
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0026_mosaicoshome_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boutique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuiaAlumnoMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.CharField(editable=False, max_length=200)),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('file', models.FileField(upload_to=cms.models.upload_to)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Mensaje guia del alumno',
                'verbose_name_plural': 'Mensajes guia del alumno',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('description', ckeditor.fields.RichTextField()),
                ('description_objetivo', ckeditor.fields.RichTextField()),
                ('image_objetivo', models.ImageField(upload_to=cms.models.upload_to)),
                ('description_resolucion', ckeditor.fields.RichTextField()),
                ('image_resolucion', models.ImageField(upload_to=cms.models.upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
