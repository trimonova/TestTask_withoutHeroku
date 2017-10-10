# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='zakaz',
            name='city',
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
        migrations.AddField(
            model_name='zakaz',
            name='place',
            field=models.CharField(max_length=255, null=True, verbose_name='Место'),
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]