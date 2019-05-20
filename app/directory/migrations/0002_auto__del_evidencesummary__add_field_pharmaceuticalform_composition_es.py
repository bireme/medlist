# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EvidenceSummary'
        db.delete_table('directory_evidencesummary')

        # Adding field 'PharmaceuticalForm.composition_es'
        db.add_column('directory_pharmaceuticalform', 'composition_es',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'PharmaceuticalForm.composition_pt'
        db.add_column('directory_pharmaceuticalform', 'composition_pt',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'EvidenceSummary'
        db.create_table('directory_evidencesummary', (
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('link', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('context', self.gf('django.db.models.fields.TextField')()),
            ('medicine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Medicine'])),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('directory', ['EvidenceSummary'])

        # Deleting field 'PharmaceuticalForm.composition_es'
        db.delete_column('directory_pharmaceuticalform', 'composition_es')

        # Deleting field 'PharmaceuticalForm.composition_pt'
        db.delete_column('directory_pharmaceuticalform', 'composition_pt')

    models = {
        'directory.medicine': {
            'Meta': {'object_name': 'Medicine'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'directory.medicinelocal': {
            'Meta': {'object_name': 'MedicineLocal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Medicine']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'directory.pharmaceuticalform': {
            'Meta': {'object_name': 'PharmaceuticalForm'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'atc_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'composition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'composition_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'composition_pt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Medicine']"}),
            'pharmaceutical_form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.PharmaceuticalFormType']"})
        },
        'directory.pharmaceuticalformtype': {
            'Meta': {'object_name': 'PharmaceuticalFormType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'directory.pharmaceuticalformtypelocal': {
            'Meta': {'object_name': 'PharmaceuticalFormTypeLocal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pharmaceutical_form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.PharmaceuticalFormType']"})
        }
    }

    complete_apps = ['directory']