# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-27 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_management', '0010_remove_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='expense2',
            name='Price',
            field=models.CharField(max_length=250),
        ),
    ]