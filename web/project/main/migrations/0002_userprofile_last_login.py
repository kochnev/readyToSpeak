# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-04 10:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 10, 39, 38, 265575, tzinfo=utc)),
        ),
    ]
