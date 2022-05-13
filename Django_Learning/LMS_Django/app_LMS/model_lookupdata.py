# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class LmsMdLookup(models.Model):
    serialno = models.AutoField(db_column='serialNo', primary_key=True)  # Field name made lowercase.
    cs_start = models.IntegerField(blank=True, null=True)
    cs_end = models.IntegerField(blank=True, null=True)
    loan_amt_start = models.IntegerField(blank=True, null=True)
    loan_amt_end = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    interest = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lms_md_lookup'
