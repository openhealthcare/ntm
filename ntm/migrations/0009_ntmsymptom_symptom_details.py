# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntm', '0008_auto_20170313_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntmsymptom',
            name='symptom_details',
            field=models.TextField(null=True, verbose_name=b'details', blank=True),
        ),
    ]
