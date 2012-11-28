# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoryLocal'
        db.create_table('history_historylocal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['list.List'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('obs', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('xml', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('history', ['HistoryLocal'])

        # Adding field 'History.abbreviation'
        db.add_column('history_history', 'abbreviation',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'History.edition'
        db.add_column('history_history', 'edition',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'History.published'
        db.add_column('history_history', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'History.obs'
        db.add_column('history_history', 'obs',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'History.xml'
        db.add_column('history_history', 'xml',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'History.subtype'
        db.alter_column('history_history', 'subtype', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'History.year'
        db.alter_column('history_history', 'year', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'History.type'
        db.alter_column('history_history', 'type', self.gf('django.db.models.fields.CharField')(max_length=1))
    def backwards(self, orm):
        # Deleting model 'HistoryLocal'
        db.delete_table('history_historylocal')

        # Deleting field 'History.abbreviation'
        db.delete_column('history_history', 'abbreviation')

        # Deleting field 'History.edition'
        db.delete_column('history_history', 'edition')

        # Deleting field 'History.published'
        db.delete_column('history_history', 'published')

        # Deleting field 'History.obs'
        db.delete_column('history_history', 'obs')

        # Deleting field 'History.xml'
        db.delete_column('history_history', 'xml')


        # Changing field 'History.subtype'
        db.alter_column('history_history', 'subtype', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'History.year'
        db.alter_column('history_history', 'year', self.gf('django.db.models.fields.CharField')(max_length=4))

        # Changing field 'History.type'
        db.alter_column('history_history', 'type', self.gf('django.db.models.fields.CharField')(max_length=255))
    models = {
        'history.history': {
            'Meta': {'object_name': 'History'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subtype': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'xml': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'history.historylocal': {
            'Meta': {'object_name': 'HistoryLocal'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'xml': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'list.list': {
            'Meta': {'object_name': 'List'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subtype': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['history']