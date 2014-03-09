# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ask'
        db.create_table(u'help_ask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'help', ['Ask'])

        # Adding model 'Answer'
        db.create_table(u'help_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('ask', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['help.Ask'])),
        ))
        db.send_create_signal(u'help', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Ask'
        db.delete_table(u'help_ask')

        # Deleting model 'Answer'
        db.delete_table(u'help_answer')


    models = {
        u'help.answer': {
            'Meta': {'object_name': 'Answer'},
            'ask': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['help.Ask']"}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'help.ask': {
            'Meta': {'object_name': 'Ask'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['help']