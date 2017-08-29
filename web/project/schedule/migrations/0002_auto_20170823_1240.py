# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-23 12:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyschedule',
            name='dt_from',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 12, 40, 47, 465435, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklyschedule',
            name='dt_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
