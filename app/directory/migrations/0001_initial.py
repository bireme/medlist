# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Medicine'
        db.create_table('directory_medicine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('directory', ['Medicine'])

        # Adding model 'MedicineLocal'
        db.create_table('directory_medicinelocal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medicine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Medicine'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['MedicineLocal'])

        # Adding model 'EvidenceSummary'
        db.create_table('directory_evidencesummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medicine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Medicine'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('context', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('directory', ['EvidenceSummary'])

        # Adding model 'PharmaceuticalFormType'
        db.create_table('directory_pharmaceuticalformtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('directory', ['PharmaceuticalFormType'])

        # Adding model 'PharmaceuticalFormTypeLocal'
        db.create_table('directory_pharmaceuticalformtypelocal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pharmaceutical_form_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.PharmaceuticalFormType'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['PharmaceuticalFormTypeLocal'])

        # Adding model 'PharmaceuticalForm'
        db.create_table('directory_pharmaceuticalform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medicine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Medicine'])),
            ('pharmaceutical_form_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.PharmaceuticalFormType'])),
            ('atc_code', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('composition', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('directory', ['PharmaceuticalForm'])


    def backwards(self, orm):
        
        # Deleting model 'Medicine'
        db.delete_table('directory_medicine')

        # Deleting model 'MedicineLocal'
        db.delete_table('directory_medicinelocal')

        # Deleting model 'EvidenceSummary'
        db.delete_table('directory_evidencesummary')

        # Deleting model 'PharmaceuticalFormType'
        db.delete_table('directory_pharmaceuticalformtype')

        # Deleting model 'PharmaceuticalFormTypeLocal'
        db.delete_table('directory_pharmaceuticalformtypelocal')

        # Deleting model 'PharmaceuticalForm'
        db.delete_table('directory_pharmaceuticalform')


    models = {
        'directory.evidencesummary': {
            'Meta': {'object_name': 'EvidenceSummary'},
            'context': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medicine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Medicine']"}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
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
