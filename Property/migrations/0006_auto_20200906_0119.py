# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-06 01:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0005_auto_20200906_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='User.Seller'),
        ),
    ]
