# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171011_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='waiters',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.OrderPlace', verbose_name='Место работы'),
        ),
    ]