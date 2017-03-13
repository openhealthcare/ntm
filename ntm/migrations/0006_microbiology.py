# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ntm', '0005_auto_20170313_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microbiology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('date_of_sample', models.DateField(null=True, blank=True)),
                ('specimen_type', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Sputum', b'Sputum'), (b'BAL', b'BAL'), (b'Bronchial washing', b'Bronchial washing'), (b'Blood', b'Blood'), (b'Tissue Biopsy', b'Tissue Biopsy'), (b'Needle Aspirate', b'Needle Aspirate')])),
                ('mycrobacterium_avium', models.BooleanField(default=False)),
                ('mycrbacterium_intracellulare', models.BooleanField(default=False)),
                ('mycrbacterium_kansasil', models.BooleanField(default=False)),
                ('mycrbacterium_abcessus', models.BooleanField(default=False)),
                ('mycrbacterium_chelonae', models.BooleanField(default=False)),
                ('mycrbacterium_fortuitum', models.BooleanField(default=False)),
                ('mycrbacterium_genavense', models.BooleanField(default=False)),
                ('mycrbacterium_gordonae', models.BooleanField(default=False)),
                ('mycrbacterium_haemophilum', models.BooleanField(default=False)),
                ('mycrbacterium_immunogenum', models.BooleanField(default=False)),
                ('mycrbacterium_malmoense', models.BooleanField(default=False)),
                ('mycrbacterium_marinum', models.BooleanField(default=False)),
                ('mycrbacterium_mucogenicum', models.BooleanField(default=False)),
                ('mycrbacterium_nonchromogenicum', models.BooleanField(default=False)),
                ('mycrbacterium_scrofulaceum', models.BooleanField(default=False)),
                ('mycrbacterium_simiae', models.BooleanField(default=False)),
                ('mycrbacterium_smegmatis', models.BooleanField(default=False)),
                ('mycrbacterium_szulgai', models.BooleanField(default=False)),
                ('mycrbacterium_terrae', models.BooleanField(default=False)),
                ('mycrbacterium_ulcerans', models.BooleanField(default=False)),
                ('mycrbacterium_xenopi', models.BooleanField(default=False)),
                ('mycrbacterium_tuberculosis', models.BooleanField(default=False)),
                ('pseudamonas_aeroginosa', models.BooleanField(default=False)),
                ('steptoccocus_sp', models.BooleanField(default=False)),
                ('staphylococcus_sp', models.BooleanField(default=False)),
                ('enterococcus_sp', models.BooleanField(default=False)),
                ('haemophilus_influenzae', models.BooleanField(default=False)),
                ('klebsiella_pneumoniae', models.BooleanField(default=False)),
                ('enterobacter', models.BooleanField(default=False)),
                ('Aspergillus', models.BooleanField(default=False)),
                ('moraxella', models.BooleanField(default=False)),
                ('other', models.CharField(max_length=256, null=True, blank=True)),
                ('time_to_positive', models.CharField(max_length=256, null=True, verbose_name=b'Time to positive_culture (days)', blank=True)),
                ('subspecies', models.CharField(max_length=256, null=True, verbose_name=b'Supspecies if known', blank=True)),
                ('identification_methods', models.TextField(null=True, verbose_name=b'Species identification methods used', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_microbiology_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_microbiology_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
