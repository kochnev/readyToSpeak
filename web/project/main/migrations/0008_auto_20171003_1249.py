# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20171003_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=5),
        ),
    ]
