# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20161122_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]