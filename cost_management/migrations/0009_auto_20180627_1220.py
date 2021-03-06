# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-27 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cost_management', '0008_expense2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense2',
            name='date',
        ),
        migrations.RemoveField(
            model_name='expense2',
            name='id',
        ),
        migrations.AddField(
            model_name='expense2',
            name='expense_ptr',
            field=models.OneToOneField(auto_created=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cost_management.Expense'),
            preserve_default=False,
        ),
    ]
