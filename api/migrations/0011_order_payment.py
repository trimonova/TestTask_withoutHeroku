# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_order_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.NullBooleanField(),
        ),
    ]
