# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170627_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='ext_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]