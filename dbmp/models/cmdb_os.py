#-*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class CmdbOs(models.Model):
    os_id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=50)
    alias = models.CharField(max_length=40)
    ip = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    remark = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Java toString 方法"""
        print_str = 'ip({ip}), hostname({hostname}), alias({alias})'.format(
                     ip = self.ip,
                     hostname = self.hostname,
                     alias = self.alias)
        return print_str

    class Meta:
        managed = False
        db_table = 'cmdb_os'
