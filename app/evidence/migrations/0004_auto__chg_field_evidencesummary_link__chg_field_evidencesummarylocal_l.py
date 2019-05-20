# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EvidenceSummary.link'
        db.alter_column('evidence_evidencesummary', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'EvidenceSummaryLocal.link'
        db.alter_column('evidence_evidencesummarylocal', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))
    def backwards(self, orm):

        # Changing field 'EvidenceSummary.link'
        db.alter_column('evidence_evidencesummary', 'link', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'EvidenceSummaryLocal.link'
        db.alter_column('evidence_evidencesummarylocal', 'link', self.gf('django.db.models.fields.CharField')(max_length=255))
    models = {
        'directory.medicine': {
            'Meta': {'object_name': 'Medicine'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'evidence.evidencesummary': {
            'Meta': {'object_name': 'EvidenceSummary'},
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['directory.Medicine']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 0, 0)'})
        },
        'evidence.evidencesummarylocal': {
            'Meta': {'object_name': 'EvidenceSummaryLocal'},
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['evidence.EvidenceSummary']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 0, 0)'})
        }
    }

    complete_apps = ['evidence']