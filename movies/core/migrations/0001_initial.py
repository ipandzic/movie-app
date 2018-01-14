# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('production_company', models.CharField(blank=True, max_length=1024, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('movie_url', models.CharField(blank=True, max_length=1024, null=True)),
                ('image_url', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
