# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 23:12
from __future__ import unicode_literals

import ckeditor.fields
import cms.models
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarreraDeCine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('message_title', models.CharField(max_length=140)),
                ('message_body', ckeditor.fields.RichTextField()),
                ('second_description', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cortometrajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='CursosTalleres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('message_title', models.CharField(max_length=140)),
                ('message_body', ckeditor.fields.RichTextField()),
                ('second_description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Filmografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='OperasPrimas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('second_description', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperasPrimasEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('avatart', models.ImageField(upload_to=cms.models.upload_to)),
                ('role', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanDeEstudios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Productora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('second_description', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Temario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', ckeditor.fields.RichTextField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.CursosTalleres')),
            ],
        ),
    ]
