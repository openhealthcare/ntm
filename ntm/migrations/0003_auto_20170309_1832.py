# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ntm', '0002_smokinghistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('bmi', models.CharField(max_length=256, null=True, blank=True)),
                ('other_immunodeficiency', models.CharField(max_length=256, null=True, blank=True)),
                ('details_of_immunosupressive_drug_therapy', models.TextField(null=True, blank=True)),
                ('immunosuppression_indication', models.CharField(max_length=256, null=True, blank=True)),
                ('immunosuppression_duration', models.CharField(max_length=256, null=True, blank=True)),
                ('rhematoid_arthritis', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Adult', b'Adult'), (b'Juvenile', b'Juvenile')])),
                ('serongative_arthritis', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Psoriatic arthritis', b'Psoriatic arthritis'), (b'IBD', b'IBD'), (b'Ankylosing spondylitis', b'Ankylosing spondylitis'), (b'Other', b'Other')])),
                ('other_rheumatological_condition', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Vasculitis', b'Vasculitis'), (b'SLE', b'SLE'), (b'Scleredema', b'Scleredema'), (b"Sjogren's", b"Sjogren's"), (b"Becet's", b"Becet's"), (b"Wegener's/GPA", b"Wegener's/GPA"), (b'Anti-phospholipid syndrome', b'Anti-phospholipid syndrome'), (b'Other', b'Other')])),
                ('active_malignancy', models.NullBooleanField()),
                ('past_malignancy', models.NullBooleanField()),
                ('malignancy_type', models.CharField(max_length=256, null=True, blank=True)),
                ('ntm_risk_factors_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('secondary_immunodeficiency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('primary_immunodeficiency_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('respiratory_history_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_clinicalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NtmRiskFactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrimaryImmunodeficiencyOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RespiratoryHistoryOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecondaryImmunodeficiencyOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='clinicalhistory',
            name='ntm_risk_factors_fk',
            field=models.ForeignKey(blank=True, to='ntm.NtmRiskFactor', null=True),
        ),
        migrations.AddField(
            model_name='clinicalhistory',
            name='patient',
            field=models.ForeignKey(to='opal.Patient'),
        ),
        migrations.AddField(
            model_name='clinicalhistory',
            name='primary_immunodeficiency_fk',
            field=models.ForeignKey(blank=True, to='ntm.PrimaryImmunodeficiencyOptions', null=True),
        ),
        migrations.AddField(
            model_name='clinicalhistory',
            name='respiratory_history_fk',
            field=models.ForeignKey(blank=True, to='ntm.RespiratoryHistoryOptions', null=True),
        ),
        migrations.AddField(
            model_name='clinicalhistory',
            name='secondary_immunodeficiency_fk',
            field=models.ForeignKey(blank=True, to='ntm.SecondaryImmunodeficiencyOptions', null=True),
        ),
        migrations.AddField(
            model_name='clinicalhistory',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_ntm_clinicalhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
