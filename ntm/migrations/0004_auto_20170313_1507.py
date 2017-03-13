# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ntm', '0003_auto_20170309_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancerTreatment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('chemotherapy', models.NullBooleanField()),
                ('radiotherapy', models.NullBooleanField()),
                ('type_1_diabetes_mellitus', models.BooleanField(default=False, verbose_name=b'Type 1 Diabetes Mellitus')),
                ('type_2_diabetes_mellitus', models.BooleanField(default=False, verbose_name=b'Type 2 Diabetes Mellitus')),
                ('ckd_stage_1', models.BooleanField(default=False, verbose_name=b'CKD stage 1')),
                ('ckd_stage_2', models.BooleanField(default=False, verbose_name=b'CKD stage 2')),
                ('ckd_stage_3', models.BooleanField(default=False, verbose_name=b'CKD stage 3')),
                ('ckd_stage_4', models.BooleanField(default=False, verbose_name=b'CKD stage 4')),
                ('esrf', models.BooleanField(default=False, verbose_name=b'ESRF')),
                ('gi_disease', models.BooleanField(default=False, verbose_name=b'GI disease')),
                ('cardiac_disease', models.BooleanField(default=False)),
                ('other', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_cancertreatment_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_cancertreatment_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Immunodeficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('primary', models.CharField(max_length=256, null=True, blank=True)),
                ('hiv', models.BooleanField(default=False, verbose_name=b'HIV')),
                ('use_of_tnf_alpha_blocking_agent', models.BooleanField(default=False, verbose_name=b'Use of TNF Alpha Blocking Agent')),
                ('use_of_other_immunosuppressive_medication', models.BooleanField(default=False)),
                ('solid_organ_transplant_recipient', models.BooleanField(default=False)),
                ('other_immunodeficiency', models.CharField(max_length=256, null=True, blank=True)),
                ('details_of_immunosupressive_drug_therapy', models.TextField()),
                ('immunosuppression_indication', models.TextField()),
                ('immunosuppression_duration', models.TextField()),
                ('created_by', models.ForeignKey(related_name='created_ntm_immunodeficiency_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_immunodeficiency_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Malignancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('active_malignancy', models.BooleanField(default=False)),
                ('past_malignancy', models.BooleanField(default=False)),
                ('malignancy_type', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_malignancy_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_malignancy_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NtmAssociatedRiskFactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('tall_thin_body_habitus', models.BooleanField(default=False)),
                ('hypermobility', models.BooleanField(default=False)),
                ('mv_prolapse', models.BooleanField(default=False, verbose_name=b'MV prolapse')),
                ('oesophageal_dysmobility', models.BooleanField(default=False)),
                ('gastro_oesophageal_reflux_disease', models.BooleanField(default=False, verbose_name=b'Gastro-oesophageal_reflux_disease')),
                ('other', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='created_ntm_ntmassociatedriskfactor_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_ntmassociatedriskfactor_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NtmSymptom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('breathlessness', models.BooleanField(default=False)),
                ('cough', models.BooleanField(default=False)),
                ('sputum', models.BooleanField(default=False)),
                ('fatigue', models.BooleanField(default=False)),
                ('fevers', models.BooleanField(default=False)),
                ('night_sweats', models.BooleanField(default=False)),
                ('weight_loss', models.BooleanField(default=False)),
                ('gi_symptoms', models.BooleanField(default=False, verbose_name=b'GI symptoms')),
                ('haemoptysis', models.BooleanField(default=False)),
                ('rash', models.BooleanField(default=False)),
                ('Lymphadenopathy', models.BooleanField(default=False)),
                ('skin_infection', models.BooleanField(default=False, verbose_name=b'Skin/soft tissue infection')),
                ('recurrent_chest_infections', models.BooleanField(default=False)),
                ('other', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_ntmsymptom_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_ntmsymptom_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OtherObservations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('bmi', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_otherobservations_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_otherobservations_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RespiratoryHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('previous_ntm_infection', models.BooleanField(default=False, verbose_name=b'Previous NTM Infection')),
                ('previous_tb_infection', models.BooleanField(default=False, verbose_name=b'Previous TB Infection')),
                ('alpha_1_antitypsis_deficiency', models.BooleanField(default=False, verbose_name=b'Alpha-1 Antitrypsin Deficiency')),
                ('pneumoconiosis', models.BooleanField(default=False)),
                ('primary_ciliary_dyskinesia', models.BooleanField(default=False)),
                ('pulmonary_alveolar_proteinosis', models.BooleanField(default=False)),
                ('silicosis', models.BooleanField(default=False)),
                ('other', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_respiratoryhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_respiratoryhistory_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Rheumatology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('rhematoid_arthritis', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Adult', b'Adult'), (b'Juvenile', b'Juvenile')])),
                ('serongative_arthritis', models.CharField(blank=True, max_length=256, null=True, choices=[(b'Psoriatic arthritis', b'Psoriatic arthritis'), (b'IBD', b'IBD'), (b'Ankylosing spondylitis', b'Ankylosing spondylitis'), (b'Other', b'Other')])),
                ('vasculitis', models.BooleanField(default=False)),
                ('sle', models.BooleanField(default=False, verbose_name=b'SLE')),
                ('scleredema', models.BooleanField(default=False)),
                ('sjogren', models.BooleanField(default=False, verbose_name=b"Sjogren's")),
                ('becet', models.BooleanField(default=False, verbose_name=b"Becet's")),
                ('wegener', models.BooleanField(default=False, verbose_name=b"Wegener's/GPA")),
                ('anti_phospholipid_syndrome', models.BooleanField(default=False, verbose_name=b'Anti-phospholipid syndrome')),
                ('other', models.CharField(max_length=256, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_ntm_rheumatology_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_ntm_rheumatology_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='ntm_risk_factors_fk',
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='primary_immunodeficiency_fk',
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='respiratory_history_fk',
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='secondary_immunodeficiency_fk',
        ),
        migrations.RemoveField(
            model_name='clinicalhistory',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='ClinicalHistory',
        ),
        migrations.DeleteModel(
            name='NtmRiskFactor',
        ),
        migrations.DeleteModel(
            name='PrimaryImmunodeficiencyOptions',
        ),
        migrations.DeleteModel(
            name='RespiratoryHistoryOptions',
        ),
        migrations.DeleteModel(
            name='SecondaryImmunodeficiencyOptions',
        ),
    ]
