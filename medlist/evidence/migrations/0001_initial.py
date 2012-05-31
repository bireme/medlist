# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EvidenceSummary'
        db.create_table('evidence_evidencesummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medicine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['directory.Medicine'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 31, 17, 34, 22, 94685))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 31, 17, 34, 22, 94729))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('context', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('evidence', ['EvidenceSummary'])

        # Adding model 'EvidenceSummaryLocal'
        db.create_table('evidence_evidencesummarylocal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evidence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evidence.EvidenceSummary'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 31, 17, 34, 22, 95611))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 31, 17, 34, 22, 95642))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('context', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('evidence', ['EvidenceSummaryLocal'])


    def backwards(self, orm):
        
        # Deleting model 'EvidenceSummary'
        db.delete_table('evidence_evidencesummary')

        # Deleting model 'EvidenceSummaryLocal'
        db.delete_table('evidence_evidencesummarylocal')


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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 31, 17, 34, 22, 94685)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['directory.Medicine']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 31, 17, 34, 22, 94729)'})
        },
        'evidence.evidencesummarylocal': {
            'Meta': {'object_name': 'EvidenceSummaryLocal'},
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 31, 17, 34, 22, 95611)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['evidence.EvidenceSummary']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 31, 17, 34, 22, 95642)'})
        }
    }

    complete_apps = ['evidence']
