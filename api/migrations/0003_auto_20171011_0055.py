# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171011_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderline',
            options={},
        ),
        migrations.AlterField(
            model_name='orderline',
            name='count',
            field=models.IntegerField(default=0, null=True, verbose_name='Строка заказа'),
        ),
    ]
