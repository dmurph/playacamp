# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_add_is_verified_by_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceprofile',
            name='arrival_date',
            field=models.CharField(blank=True, choices=[('wednesday1', 'Wednesday (Early)'), ('thursday1', 'Thursday (Early)'), ('friday1', 'Friday (Early)'), ('saturday', 'Saturday (Early)'), ('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday2', 'Wednesday'), ('thursday2', 'Thursday'), ('friday2', 'Friday')], max_length=16, null=True),
        ),
    ]