# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ntm', '0006_microbiology'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTFindings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('date_of_ct_scan', models.DateField(null=True, blank=True)),
                ('bronchiectasis_segments', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Bronchiectasis (bronchopulmonary segments)', choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('bronchiectasis_severity', models.CharField(blank=True, max_length=256, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('nodules', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Nodules (>5mm)', choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('tree_in_bud', models.CharField(blank=True, max_length=256, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('central_mucous_plugging', models.CharField(blank=True, max_length=256, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('consolidation2', models.CharField(blank=True, max_length=256, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('mosaicism', models.CharField(blank=True, max_length=256, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('cavitation_of_nodules', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('severe_cavitation_of_nodules', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('aspergilloma', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('created_by', models.ForeignKey(related_name='created_ntm_ctfindings_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_ctfindings_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Xray',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('date_of_chest_xray', models.DateField(null=True, verbose_name=b'Date of Chest X-Ray', blank=True)),
                ('bronchiectasis', models.CharField(blank=True, max_length=256, null=True, choices=[(b'RUZ', b'RUZ'), (b'RMZ', b'RMZ'), (b'RLZ', b'RLZ'), (b'LUZ', b'LUZ'), (b'LMZ', b'LMZ'), (b'LLZ', b'LLZ'), (b'Upper zones', b'Upper zones'), (b'Mid zones', b'Mid zones'), (b'Lower zones', b'Lower zones'), (b'Other', b'Other')])),
                ('nodules', models.CharField(blank=True, max_length=256, null=True, choices=[(b'RUZ', b'RUZ'), (b'RMZ', b'RMZ'), (b'RLZ', b'RLZ'), (b'LUZ', b'LUZ'), (b'LMZ', b'LMZ'), (b'LLZ', b'LLZ'), (b'Upper zones', b'Upper zones'), (b'Mid zones', b'Mid zones'), (b'Lower zones', b'Lower zones'), (b'Other', b'Other')])),
                ('consoliation', models.CharField(blank=True, max_length=256, null=True, choices=[(b'RUZ', b'RUZ'), (b'RMZ', b'RMZ'), (b'RLZ', b'RLZ'), (b'LUZ', b'LUZ'), (b'LMZ', b'LMZ'), (b'LLZ', b'LLZ'), (b'Upper zones', b'Upper zones'), (b'Mid zones', b'Mid zones'), (b'Lower zones', b'Lower zones'), (b'Other', b'Other')])),
                ('caviation', models.CharField(blank=True, max_length=256, null=True, choices=[(b'RUZ', b'RUZ'), (b'RMZ', b'RMZ'), (b'RLZ', b'RLZ'), (b'LUZ', b'LUZ'), (b'LMZ', b'LMZ'), (b'LLZ', b'LLZ'), (b'Upper zones', b'Upper zones'), (b'Mid zones', b'Mid zones'), (b'Lower zones', b'Lower zones'), (b'Other', b'Other')])),
                ('other', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_xray_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_xray_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
