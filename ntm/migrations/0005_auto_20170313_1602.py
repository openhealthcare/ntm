# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntm', '0004_auto_20170313_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntmsymptom',
            name='cough_type',
            field=models.CharField(blank=True, max_length=256, null=True, choices=[(b'Dry', b'Dry'), (b'Wet', b'Wet')]),
        ),
        migrations.AddField(
            model_name='ntmsymptom',
            name='excercise_tolerence',
            field=models.CharField(max_length=256, null=True, verbose_name=b'Excercie tolerence (metres on the flat)', blank=True),
        ),
        migrations.AddField(
            model_name='ntmsymptom',
            name='sputum_colour',
            field=models.CharField(blank=True, max_length=256, null=True, choices=[(b'Clear', b'Clear'), (b'Frothy', b'Frothy'), (b'Pink', b'Pink'), (b'Yellow', b'Yellow'), (b'Green', b'Green'), (b'Brown', b'Brown'), (b'Blood-streaked', b'Blood-streaked')]),
        ),
        migrations.AddField(
            model_name='ntmsymptom',
            name='weight_loss_details',
            field=models.TextField(null=True, blank=True),
        ),
    ]
