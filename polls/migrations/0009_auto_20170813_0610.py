# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-13 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170812_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestletter',
            name='receiver',
        ),
        migrations.AddField(
            model_name='requestletter',
            name='receiver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Neighbor'),
        ),
    ]
