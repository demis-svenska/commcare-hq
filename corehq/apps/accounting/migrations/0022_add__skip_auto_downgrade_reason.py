# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-14 12:33
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0021_standard_user_limit_march_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='skip_auto_downgrade_reason',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]