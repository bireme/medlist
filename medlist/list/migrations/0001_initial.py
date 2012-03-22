# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'List'
        db.create_table('list_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('subtype', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('list', ['List'])

        # Adding model 'Section'
        db.create_table('list_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['list.Section'])),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['list.List'])),
            ('complementary_list', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('list', ['Section'])

        # Adding model 'SectionPharmForm'
        db.create_table('list_sectionpharmform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['list.Section'])),
            ('pharmaceutical_form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.PharmaceuticalForm'])),
            ('only_for_children', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('specialist_care_for_children', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('restriction_age', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('list', ['SectionPharmForm'])


    def backwards(self, orm):
        
        # Deleting model 'List'
        db.delete_table('list_list')

        # Deleting model 'Section'
        db.delete_table('list_section')

        # Deleting model 'SectionPharmForm'
        db.delete_table('list_sectionpharmform')


    models = {
        'directory.medicine': {
            'Meta': {'object_name': 'Medicine'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'list.list': {
            'Meta': {'object_name': 'List'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subtype': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'list.section': {
            'Meta': {'object_name': 'Section'},
            'complementary_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.List']"}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['list.Section']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'list.sectionpharmform': {
            'Meta': {'object_name': 'SectionPharmForm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'only_for_children': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pharmaceutical_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.PharmaceuticalForm']"}),
            'restriction_age': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.Section']"}),
            'specialist_care_for_children': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['list']
