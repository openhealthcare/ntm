# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        ('ntm', '0007_ctfindings_xray'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='Lymphadenopathy',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='breathlessness',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='cough',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='fatigue',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='fevers',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='gi_symptoms',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='haemoptysis',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='night_sweats',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='other',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='rash',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='recurrent_chest_infections',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='skin_infection',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='sputum',
        ),
        migrations.RemoveField(
            model_name='ntmsymptom',
            name='weight_loss',
        ),
        migrations.AddField(
            model_name='ntmsymptom',
            name='symptoms',
            field=models.ManyToManyField(related_name='ntm_symptoms', to='opal.Symptom', blank=True),
        ),
    ]
