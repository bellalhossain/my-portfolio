# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-24 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cost_management', '0004_auto_20170214_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='purpose',
            new_name='Bookname',
        ),
    ]
