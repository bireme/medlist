# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'List.edition'
        db.add_column('list_list', 'edition',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'List.edition'
        db.delete_column('list_list', 'edition')

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
        },
        'list.listlocal': {
            'Meta': {'object_name': 'ListLocal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.List']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'list.section': {
            'Meta': {'object_name': 'Section'},
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
        'list.sectionlocal': {
            'Meta': {'object_name': 'SectionLocal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'list.sectionpharmform': {
            'Meta': {'object_name': 'SectionPharmForm'},
            'best_evidence': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'complementary_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'observation_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'observation_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'only_for_children': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pharmaceutical_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.PharmaceuticalForm']"}),
            'restriction_age': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'restriction_age_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'restriction_age_pt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['list.Section']"}),
            'specialist_care_for_children': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['list']