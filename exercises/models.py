from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.contrib.postgres.fields import ArrayField

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

DROPDOWN_CHOICES = [
    ('Increases','Increases'),
    ('Decreases', 'Decreases'),
    ('Same', 'Stays Same'),
]

class StudentsDb(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    vs_dropdown = models.CharField(max_length=50, choices=DROPDOWN_CHOICES, blank=False, null=True)
    r1_dropdown = models.CharField(max_length=50, choices=DROPDOWN_CHOICES, blank=False, null=True)
    r2_dropdown = models.CharField(max_length=50, choices=DROPDOWN_CHOICES, blank=False, null=True)
    r3_dropdown = models.CharField(max_length=50, choices=DROPDOWN_CHOICES, blank=False, null=True)
    r4_dropdown = models.CharField(max_length=50, choices=DROPDOWN_CHOICES, blank=False, null=True)
    r4_dropdown = models.CharField(max_length=50,  default='Select', blank=True, null=True)
    raw_response = models.TextField(blank=True, null=True)
    processed_response = models.TextField(blank=True, null=True)
    feedback_on_feedback = models.TextField(blank=True, null=True)
    pre_confidence = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    pre_ability = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    post_confidence = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    post_ability = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    least_confident = models.TextField(blank=True, null=True)
    most_confident = models.TextField(blank=True, null=True)
    time_started = models.DateTimeField(auto_now_add=True)
    time_finished = models.DateTimeField(auto_now_add=True)
    localized_power = ArrayField(models.CharField(max_length=1))
    ideal_vs_properties = ArrayField(models.CharField(max_length=1))
    seq_current_direction = models.CharField(max_length=10, blank=True, null=True)
    seq_current_relationship = models.TextField(blank=True, null=True)
    seq_resistor_vdrop = ArrayField(models.CharField(max_length=1))
    constantVdrop_vdrop = ArrayField(models.CharField(max_length=1))
    constantVdrop_kvl = models.CharField(max_length=10, blank=True, null=True)
    resistorCombo_series = ArrayField(models.CharField(max_length=1))
    energyCons_energy = ArrayField(models.CharField(max_length=1))
    correctPath_ser_par = ArrayField(models.CharField(max_length=1))
    correctPath_eff_resistance = models.CharField(max_length=10, blank=True, null=True)
    correctPath_idealVs = ArrayField(models.CharField(max_length=1))
    correctPath_R1 = ArrayField(models.CharField(max_length=1))
    correctPath_R23 = ArrayField(models.CharField(max_length=1))
    correctPath_R2_short = ArrayField(models.CharField(max_length=1))
    correctPath_confidence = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    correctPath_feedback_on_feedback = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'students_db'

class FocusUser(AbstractUser):
    focus_req = models.BooleanField(default=False)