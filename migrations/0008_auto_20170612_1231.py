# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-12 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0007_auto_20170612_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco_events',
            name='streamname',
            field=models.CharField(max_length=20),
        ),
    ]
