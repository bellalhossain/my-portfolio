# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurants', '0004_auto_20180616_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
