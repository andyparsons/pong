# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Help.ask'
        db.add_column(u'main_help', 'ask',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Ask']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Help.ask'
        db.delete_column(u'main_help', 'ask_id')


    models = {
        u'main.ask': {
            'Meta': {'object_name': 'Ask'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'main.help': {
            'Meta': {'object_name': 'Help'},
            'ask': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Ask']"}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['main']