# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sector_datamigration', '0009_auto_20170418_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='patientWeight',
            field=models.DecimalField(decimal_places=10, max_digits=18),
        ),
    ]
