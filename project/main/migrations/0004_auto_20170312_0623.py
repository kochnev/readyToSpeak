# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170312_0623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlanguage',
            old_name='isnative',
            new_name='native',
        ),
    ]