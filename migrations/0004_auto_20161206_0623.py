# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-06 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0003_auto_20161205_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='congestion_alarms',
            old_name='diffMedian',
            new_name='diffmedian',
        ),
        migrations.RenameField(
            model_name='congestion_alarms',
            old_name='nbProbes',
            new_name='nbprobes',
        ),
        migrations.RenameField(
            model_name='forwarding_alarms',
            old_name='pktDiff',
            new_name='pktdiff',
        ),
        migrations.RenameField(
            model_name='forwarding_alarms',
            old_name='previousHop',
            new_name='previoushop',
        ),
    ]
