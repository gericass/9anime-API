# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animedb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='アニメタイトル')),
                ('title_jp', models.CharField(max_length=500, verbose_name='アニメタイトル（日本語）')),
                ('year', models.CharField(max_length=500, verbose_name='放送年')),
                ('season', models.CharField(max_length=500, verbose_name='シーズン')),
                ('url', models.CharField(max_length=500, verbose_name='URL')),
            ],
        ),
    ]
