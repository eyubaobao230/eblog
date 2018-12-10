# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('icon', models.ImageField(null=True, upload_to='article')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]