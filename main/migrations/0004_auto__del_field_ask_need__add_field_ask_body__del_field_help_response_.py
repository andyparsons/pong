# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ask.need'
        db.delete_column(u'main_ask', 'need')

        # Adding field 'Ask.body'
        db.add_column(u'main_ask', 'body',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)

        # Deleting field 'Help.response'
        db.delete_column(u'main_help', 'response')

        # Adding field 'Help.body'
        db.add_column(u'main_help', 'body',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Ask.need'
        db.add_column(u'main_ask', 'need',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)

        # Deleting field 'Ask.body'
        db.delete_column(u'main_ask', 'body')

        # Adding field 'Help.response'
        db.add_column(u'main_help', 'response',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)

        # Deleting field 'Help.body'
        db.delete_column(u'main_help', 'body')


    models = {
        u'main.ask': {
            'Meta': {'object_name': 'Ask'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'main.help': {
            'Meta': {'object_name': 'Help'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['main']