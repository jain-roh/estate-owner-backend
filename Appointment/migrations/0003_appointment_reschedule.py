# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-20 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0002_auto_20200914_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='reschedule',
            field=models.IntegerField(null=True),
        ),
    ]
