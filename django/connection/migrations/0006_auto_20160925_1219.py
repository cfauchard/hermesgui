# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0005_auto_20160925_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='password',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='connection',
            name='private_key',
            field=models.FilePathField(blank=True, default=''),
        ),
    ]
