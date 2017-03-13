# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ntm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmokingHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('smoker', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Non-smoker', b'Non-smoker'), (b'Current smoker', b'Current smoker'), (b'Ex-smoker', b'Ex-smoker')])),
                ('cigarettes_per_day', models.CharField(max_length=256, null=True, blank=True)),
                ('number_of_years_smoking', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_smokinghistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_smokinghistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
