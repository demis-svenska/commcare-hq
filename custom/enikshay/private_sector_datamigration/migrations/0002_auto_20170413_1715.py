# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-13 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('private_sector_datamigration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adherence',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('adherenceId', models.CharField(max_length=18, null=True, unique=True)),
                ('commentId', models.CharField(max_length=8, null=True)),
                ('creationDate', models.DateTimeField(null=True)),
                ('creator', models.CharField(max_length=255, null=True)),
                ('dosageStatusId', models.IntegerField()),
                ('doseDate', models.DateTimeField()),
                ('doseReasonId', models.IntegerField()),
                ('modificationDate', models.DateTimeField(null=True)),
                ('modifiedBy', models.CharField(max_length=255, null=True)),
                ('owner', models.CharField(max_length=255, null=True)),
                ('reportingMechanismId', models.IntegerField()),
                ('unknwDoseReasonId', models.CharField(max_length=8, null=True)),
                ('beneficiaryId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='private_sector_datamigration.Beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accountName', models.CharField(max_length=255, null=True)),
                ('accountType', models.CharField(max_length=255, null=True)),
                ('adherenceScore', models.DecimalField(decimal_places=10, max_digits=12)),
                ('alertFrequencyId', models.IntegerField()),
                ('associatedFO', models.CharField(max_length=255, null=True)),
                ('bankName', models.CharField(max_length=255, null=True)),
                ('basisOfDiagnosis', models.CharField(max_length=255, null=True)),
                ('beneficiaryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='private_sector_datamigration.Beneficiary')),
                ('branchName', models.CharField(max_length=255, null=True)),
                ('creationDate', models.DateTimeField(null=True)),
                ('creator', models.CharField(max_length=255, null=True)),
                ('dateOfDiagnosis', models.DateTimeField(null=True)),
                ('diabetes', models.CharField(max_length=255, null=True)),
                ('dstStatus', models.CharField(max_length=255, null=True)),
                ('episodeDisplayID', models.IntegerField()),
                ('episodeID', models.CharField(max_length=8, null=True)),
                ('extraPulmonary', models.CharField(max_length=255, null=True)),
                ('hiv', models.CharField(max_length=255, null=True)),
                ('ifscCode', models.CharField(max_length=255, null=True)),
                ('isNonSuperVisor', models.CharField(max_length=255, null=True)),
                ('lastMonthAdherencePct', models.DecimalField(decimal_places=10, max_digits=12)),
                ('lastTwoWeeksAdherencePct', models.DecimalField(decimal_places=10, max_digits=12)),
                ('micr', models.CharField(max_length=255, null=True)),
                ('missedDosesPct', models.DecimalField(decimal_places=10, max_digits=12)),
                ('mobileNumber', models.CharField(max_length=255, null=True)),
                ('modificationDate', models.DateTimeField(null=True)),
                ('modifiedBy', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('newOrRetreatment', models.CharField(max_length=255, null=True)),
                ('nikshayBy', models.CharField(max_length=255, null=True)),
                ('nikshayID', models.CharField(max_length=18, null=True)),
                ('nonRxSupervisorName', models.CharField(max_length=255, null=True)),
                ('onBeHalfOf', models.CharField(max_length=10, null=True)),
                ('organisationId', models.CharField(max_length=18, null=True)),
                ('owner', models.CharField(max_length=255, null=True)),
                ('patientWeight', models.DecimalField(decimal_places=10, max_digits=12)),
                ('phoneNumber', models.CharField(max_length=255, null=True)),
                ('retreatmentReason', models.CharField(max_length=255, null=True)),
                ('rxArchivalDate', models.DateTimeField(null=True)),
                ('rxAssignedBy', models.CharField(max_length=255, null=True)),
                ('rxInitiationStatus', models.CharField(max_length=255, null=True)),
                ('rxOutcomeDate', models.DateTimeField(null=True)),
                ('rxStartDate', models.DateTimeField(null=True)),
                ('rxSupervisor', models.CharField(max_length=255, null=True)),
                ('site', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('treatingQP', models.CharField(max_length=255, null=True)),
                ('treatmentOutcomeId', models.CharField(max_length=255, null=True)),
                ('treatmentPhase', models.CharField(max_length=255, null=True)),
                ('tsProviderType', models.CharField(max_length=255, null=True)),
                ('unknownAdherencePct', models.DecimalField(decimal_places=10, max_digits=12)),
                ('unresolvedMissedDosesPct', models.DecimalField(decimal_places=10, max_digits=12)),
                ('treatingHospital', models.CharField(max_length=10, null=True)),
                ('treatmentCompletionInsentiveFlag', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='adherence',
            name='episodeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='private_sector_datamigration.Episode'),
        ),
    ]
