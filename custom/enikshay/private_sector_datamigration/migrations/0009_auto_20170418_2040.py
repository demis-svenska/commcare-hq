# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_sector_datamigration', '0008_auto_20170418_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='adherenceScore',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episode',
            name='lastMonthAdherencePct',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episode',
            name='lastTwoWeeksAdherencePct',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episode',
            name='missedDosesPct',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episode',
            name='patientWeight',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episode',
            name='unknownAdherencePct',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episode',
            name='unresolvedMissedDosesPct',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
        migrations.AlterField(
            model_name='episodeprescription',
            name='pricePerUnit',
            field=models.DecimalField(decimal_places=10, max_digits=14),
        ),
    ]
