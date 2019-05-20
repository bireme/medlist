# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MedicineEvidenceSummary'
        db.create_table('evidence_medicineevidencesummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medicine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Medicine'])),
            ('evidence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evidence.EvidenceSummary'])),
        ))
        db.send_create_signal('evidence', ['MedicineEvidenceSummary'])


    def backwards(self, orm):
        
        # Deleting model 'MedicineEvidenceSummary'
        db.delete_table('evidence_medicineevidencesummary')


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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 16, 30, 14, 35804)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['directory.Medicine']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 16, 30, 14, 35830)'})
        },
        'evidence.evidencesummarylocal': {
            'Meta': {'object_name': 'EvidenceSummaryLocal'},
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 16, 30, 14, 36367)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['evidence.EvidenceSummary']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 1, 16, 30, 14, 36386)'})
        },
        'evidence.medicineevidencesummary': {
            'Meta': {'object_name': 'MedicineEvidenceSummary'},
            'evidence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['evidence.EvidenceSummary']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Medicine']"})
        }
    }

    complete_apps = ['evidence']
