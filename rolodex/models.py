# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'company'

    def __unicode__(self):
        return "{name}".format( name = self.name)

class Contact(models.Model):

    name    = models.CharField(max_length=150)
    company = models.ForeignKey('Company')
    note    = models.CharField(max_length=250)

    class Meta:
        db_table = 'contact'

    def __unicode__(self):
        return "{name} @ {company}".format( name = self.name, comapny = self.company.name)



