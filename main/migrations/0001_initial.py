# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ask'
        db.create_table(u'main_ask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('need', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('fulfilled', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'main', ['Ask'])


    def backwards(self, orm):
        # Deleting model 'Ask'
        db.delete_table(u'main_ask')


    models = {
        u'main.ask': {
            'Meta': {'object_name': 'Ask'},
            'fulfilled': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['main']