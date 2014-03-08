# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table(u'main_answer')

        # Adding model 'Help'
        db.create_table(u'main_help', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'main', ['Help'])


    def backwards(self, orm):
        # Adding model 'Answer'
        db.create_table(u'main_answer', (
            ('response', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'main', ['Answer'])

        # Deleting model 'Help'
        db.delete_table(u'main_help')


    models = {
        u'main.ask': {
            'Meta': {'object_name': 'Ask'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'need': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'main.help': {
            'Meta': {'object_name': 'Help'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['main']