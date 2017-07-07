# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_document_ext_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(choices=[('instructional', 'Instructional Design'), ('sales', 'Sales')], default='Instructional Design', max_length=30),
        ),
    ]