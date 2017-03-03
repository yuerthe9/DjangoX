# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('url_name', models.CharField(max_length=64, verbose_name='Url Name')),
                ('query', models.CharField(blank=True, max_length=1000, verbose_name='Query String')),
                ('is_share', models.BooleanField(default=False, verbose_name='Is Shared')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Bookmark',
                'verbose_name_plural': 'Bookmarks',
            },
        ),
        migrations.CreateModel(
            name='SystemSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=256, verbose_name='Settings Key')),
                ('value', models.TextField(verbose_name='Settings Content')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '系统设置',
                'verbose_name_plural': '系统设置',
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=256, verbose_name='Settings Key')),
                ('value', models.TextField(verbose_name='Settings Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'User Setting',
                'verbose_name_plural': 'User Settings',
            },
        ),
        migrations.CreateModel(
            name='UserWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(max_length=256, verbose_name='Page')),
                ('widget_type', models.CharField(max_length=50, verbose_name='Widget Type')),
                ('value', models.TextField(verbose_name='Widget Params')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'User Widget',
                'verbose_name_plural': 'User Widgets',
            },
        ),
    ]
