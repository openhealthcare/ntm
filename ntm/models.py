"""
ntm models.
"""
from django.db import models as fields
from opal.core import lookuplists
from opal.core.fields import ForeignKeyOrFreeText

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics):
    pass


class Location(models.Location):
    pass


class Allergies(models.Allergies):
    pass


class Diagnosis(models.Diagnosis):
    pass


class PastMedicalHistory(models.PastMedicalHistory):
    pass


class Treatment(models.Treatment):
    pass


class Investigation(models.Investigation):
    pass


class SymptomComplex(models.SymptomComplex):
    pass


class PatientConsultation(models.PatientConsultation):
    pass


class OtherObservations(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    bmi = fields.CharField(
        max_length=256, null=True, blank=True
    )


class RespiratoryHistory(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    previous_ntm_infection = fields.BooleanField(
        default=False,
        verbose_name="Previous NTM Infection"
    )
    previous_tb_infection = fields.BooleanField(
        default=False,
        verbose_name="Previous TB Infection"
    )
    alpha_1_antitypsis_deficiency = fields.BooleanField(
        default=False,
        verbose_name="Alpha-1 Antitrypsin Deficiency"
    )
    pneumoconiosis = fields.BooleanField(
        default=False,
    )
    primary_ciliary_dyskinesia = fields.BooleanField(
        default=False,
    )
    pulmonary_alveolar_proteinosis = fields.BooleanField(
        default=False,
    )
    silicosis = fields.BooleanField(
        default=False,
    )
    other = fields.CharField(
        max_length=256,
        blank=True,
        null=True
    )


class NtmAssociatedRiskFactor(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    _title = "NTM Associated Risk Factor"
    tall_thin_body_habitus = fields.BooleanField(
        default=False
    )
    hypermobility = fields.BooleanField(
        default=False
    )
    mv_prolapse = fields.BooleanField(
        default=False,
        verbose_name="MV prolapse"
    )
    oesophageal_dysmobility = fields.BooleanField(
        default=False,
    )
    gastro_oesophageal_reflux_disease = fields.BooleanField(
        default=False,
        verbose_name="Gastro-oesophageal_reflux_disease"
    )
    other = fields.BooleanField(
        default=False
    )


class Immunodeficiency(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    primary = fields.CharField(
        max_length=256, blank=True, null=True
    )
    hiv = fields.BooleanField(
        default=False,
        verbose_name="HIV"
    )
    use_of_tnf_alpha_blocking_agent = fields.BooleanField(
        default=False,
        verbose_name="Use of TNF Alpha Blocking Agent"
    )
    use_of_other_immunosuppressive_medication = fields.BooleanField(
        default=False
    )
    solid_organ_transplant_recipient = fields.BooleanField(
        default=False
    )
    other_immunodeficiency = fields.CharField(
        max_length=256,
        blank=True,
        null=True
    )
    details_of_immunosupressive_drug_therapy = fields.TextField()
    immunosuppression_indication = fields.TextField()
    immunosuppression_duration = fields.TextField()


class Rheumatology(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    RHEMATOID_ARTHRITIS_CHOICES = (
        ("Adult", "Adult"),
        ("Juvenile", "Juvenile"),
    )
    rhematoid_arthritis = fields.CharField(
        max_length=256,
        blank=True,
        null=True,
        choices=RHEMATOID_ARTHRITIS_CHOICES
    )

    SERONGATIVE_ARTHRITIS_CHOICES = (
        ("Psoriatic arthritis", "Psoriatic arthritis"),
        ("IBD", "IBD",),
        ("Ankylosing spondylitis", "Ankylosing spondylitis"),
        ("Other", "Other"),
    )

    serongative_arthritis = fields.CharField(
        max_length=256,
        blank=True,
        null=True,
        choices=SERONGATIVE_ARTHRITIS_CHOICES
    )

    # Other fields
    vasculitis = fields.BooleanField(
        default=False
    )
    sle = fields.BooleanField(
        default=False,
        verbose_name="SLE"
    )
    scleredema = fields.BooleanField(
        default=False
    )
    sjogren = fields.BooleanField(
        default=False,
        verbose_name="Sjogren's"
    )
    becet = fields.BooleanField(
        default=False,
        verbose_name="Becet's"
    )
    wegener = fields.BooleanField(
        default=False,
        verbose_name="Wegener's/GPA"
    )
    anti_phospholipid_syndrome = fields.BooleanField(
        default=False,
        verbose_name="Anti-phospholipid syndrome"
    )
    other = fields.CharField(
        max_length=256, blank=True, null=True
    )


class Malignancy(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    active_malignancy = fields.BooleanField(
        default=False
    )
    past_malignancy = fields.BooleanField(
        default=False
    )
    malignancy_type = fields.CharField(
        max_length=256, blank=True, null=True
    )



class SmokingHistory(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'

    SMOKING_CHOICES = (
        ('Non-smoker', 'Non-smoker',),
        ('Current smoker', 'Current smoker',),
        ('Ex-smoker', 'Ex-smoker',),
    )
    smoker = fields.CharField(
        choices=SMOKING_CHOICES, max_length=256, null=True, blank=True
    )
    cigarettes_per_day = fields.CharField(
        max_length=256, null=True, blank=True
    )
    number_of_years_smoking = fields.CharField(
        max_length=256, null=True, blank=True
    )


class CancerTreatment(models.PatientSubrecord):
    _icon = 'fa fa-map-marker'
    chemotherapy = fields.NullBooleanField()
    radiotherapy = fields.NullBooleanField()

    type_1_diabetes_mellitus = fields.BooleanField(
        default=False,
        verbose_name="Type 1 Diabetes Mellitus"
    )

    type_2_diabetes_mellitus = fields.BooleanField(
        default=False,
        verbose_name="Type 2 Diabetes Mellitus"
    )

    ckd_stage_1 = fields.BooleanField(
        default=False,
        verbose_name="CKD stage 1"
    )

    ckd_stage_2 = fields.BooleanField(
        default=False,
        verbose_name="CKD stage 2"
    )

    ckd_stage_3 = fields.BooleanField(
        default=False,
        verbose_name="CKD stage 3"
    )

    ckd_stage_4 = fields.BooleanField(
        default=False,
        verbose_name="CKD stage 4"
    )

    esrf = fields.BooleanField(
        default=False,
        verbose_name="ESRF"
    )

    gi_disease = fields.BooleanField(
        default=False,
        verbose_name="GI disease"
    )

    cardiac_disease = fields.BooleanField(
        default=False,
    )

    other = fields.CharField(
        max_length=256, blank=True, null=True
    )


# Clinical Presentation
class NtmSymptom(models.EpisodeSubrecord):
    _title = "Symptom"
    _icon = 'fa-stethoscope"'

    symptoms = fields.ManyToManyField(
        models.Symptom, related_name="ntm_symptoms", blank=True
    )
    symptom_details = fields.TextField(
        verbose_name="details", blank=True, null=True
    )

    excercise_tolerence = fields.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Excercie tolerence (metres on the flat)"
    )
    COUGH_TYPE_OPTIONS = (
        ('Dry', 'Dry',),
        ('Wet', 'Wet',),
    )
    cough_type = fields.CharField(
        max_length=256, blank=True, null=True, choices=COUGH_TYPE_OPTIONS
    )
    SPUTUM_COLOUR_OPTIONS = (
        ('Clear', 'Clear',),
        ('Frothy', 'Frothy',),
        ('Pink', 'Pink',),
        ('Yellow', 'Yellow',),
        ('Green', 'Green',),
        ('Brown', 'Brown',),
        ('Blood-streaked', 'Blood-streaked',),
    )
    sputum_colour = fields.CharField(
        max_length=256, blank=True, null=True, choices=SPUTUM_COLOUR_OPTIONS
    )
    weight_loss_details = fields.TextField(blank=True, null=True)

# Microbiology
class Microbiology(models.EpisodeSubrecord):
    _icon = 'fa fa-map-marker'
    date_of_sample = fields.DateField(blank=True, null=True)

    SPECIMEN_TYPE_OPTIONS = (
        ('Sputum', 'Sputum'),
        ('BAL', 'BAL'),
        ('Bronchial washing', 'Bronchial washing'),
        ('Blood', 'Blood'),
        ('Tissue Biopsy', 'Tissue Biopsy'),
        ('Needle Aspirate', 'Needle Aspirate'),
    )

    specimen_type = fields.CharField(
        max_length=256, blank=True, null=True, choices=SPECIMEN_TYPE_OPTIONS
    )

    # NTM Specis Isolated
    mycrobacterium_avium = fields.BooleanField(default=False)
    mycrbacterium_intracellulare = fields.BooleanField(default=False)
    mycrbacterium_kansasil = fields.BooleanField(default=False)
    mycrbacterium_abcessus = fields.BooleanField(default=False)
    mycrbacterium_chelonae = fields.BooleanField(default=False)
    mycrbacterium_fortuitum = fields.BooleanField(default=False)
    mycrbacterium_genavense = fields.BooleanField(default=False)
    mycrbacterium_gordonae = fields.BooleanField(default=False)
    mycrbacterium_haemophilum = fields.BooleanField(default=False)
    mycrbacterium_immunogenum = fields.BooleanField(default=False)
    mycrbacterium_malmoense = fields.BooleanField(default=False)
    mycrbacterium_marinum = fields.BooleanField(default=False)
    mycrbacterium_mucogenicum = fields.BooleanField(default=False)
    mycrbacterium_nonchromogenicum = fields.BooleanField(default=False)
    mycrbacterium_scrofulaceum = fields.BooleanField(default=False)
    mycrbacterium_simiae = fields.BooleanField(default=False)
    mycrbacterium_smegmatis = fields.BooleanField(default=False)
    mycrbacterium_szulgai = fields.BooleanField(default=False)
    mycrbacterium_terrae = fields.BooleanField(default=False)
    mycrbacterium_ulcerans = fields.BooleanField(default=False)
    mycrbacterium_xenopi = fields.BooleanField(default=False)

    # other baceria isolated
    mycrbacterium_tuberculosis = fields.BooleanField(default=False)
    pseudamonas_aeroginosa = fields.BooleanField(default=False)
    steptoccocus_sp = fields.BooleanField(default=False)
    staphylococcus_sp = fields.BooleanField(default=False)
    enterococcus_sp = fields.BooleanField(default=False)
    haemophilus_influenzae = fields.BooleanField(default=False)
    klebsiella_pneumoniae = fields.BooleanField(default=False)
    enterobacter = fields.BooleanField(default=False)
    Aspergillus = fields.BooleanField(default=False)
    moraxella = fields.BooleanField(default=False)
    other = fields.CharField(max_length=256, blank=True, null=True)
    time_to_positive = fields.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Time to positive_culture (days)"
    )
    subspecies = fields.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Supspecies if known"
    )
    identification_methods = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Species identification methods used"
    )

class Xray(models.EpisodeSubrecord):
    _title = "X-ray"
    _icon = 'fa fa-map-marker'

    date_of_chest_xray = fields.DateField(
        blank=True, null=True, verbose_name="Date of Chest X-Ray"
    )
    XRAY_CHOICES = (
        ("RUZ", "RUZ",),
        ("RMZ", "RMZ",),
        ("RLZ", "RLZ",),
        ("LUZ", "LUZ",),
        ("LMZ", "LMZ",),
        ("LLZ", "LLZ",),
        ("Upper zones", "Upper zones",),
        ("Mid zones", "Mid zones",),
        ("Lower zones", "Lower zones",),
        ("Other", "Other",),
    )
    bronchiectasis = fields.CharField(
       max_length=256, blank=True, null=True, choices=XRAY_CHOICES
    )
    nodules = fields.CharField(
       max_length=256, blank=True, null=True, choices=XRAY_CHOICES
    )
    consoliation = fields.CharField(
       max_length=256, blank=True, null=True, choices=XRAY_CHOICES
    )
    caviation = fields.CharField(
       max_length=256, blank=True, null=True, choices=XRAY_CHOICES
    )
    other = fields.TextField(blank=True, null=True)

class CTFindings(models.EpisodeSubrecord):
    _title = "CT Findings"
    _icon = 'fa fa-map-marker'

    date_of_ct_scan = fields.DateField(blank=True, null=True)
    CT_CHOICES = (
        ("0", "0",),
        ("1", "1",),
        ("2", "2",),
        ("3", "3",),
    )
    bronchiectasis_segments = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES,
       verbose_name="Bronchiectasis (bronchopulmonary segments)"
    )
    bronchiectasis_severity = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES
    )
    nodules = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES,
       verbose_name="Nodules (>5mm)"
    )
    tree_in_bud = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES
    )
    central_mucous_plugging = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES
    )
    consolidation2 = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES
    )
    mosaicism = fields.CharField(
       max_length=256, blank=True, null=True, choices=CT_CHOICES
    )

    YES_NO_CHOICES = (
        ('Yes', 'Yes',),
        ('No', 'No',),
    )

    cavitation_of_nodules = fields.CharField(
       max_length=256, blank=True, null=True, choices=YES_NO_CHOICES
    )
    severe_cavitation_of_nodules = fields.CharField(
       max_length=256, blank=True, null=True, choices=YES_NO_CHOICES
    )
    aspergilloma = fields.CharField(
       max_length=256, blank=True, null=True, choices=YES_NO_CHOICES
    )
