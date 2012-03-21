# -*- coding: utf-8 -*-
import json
from django.conf import settings
from django.core import serializers
from django.contrib import messages
from medlist.directory.models import PharmaceuticalForm, MedicineLocal
from medlist.list.models import List, Section, SectionPharmForm
from medlist.history.models import History

def create_list_archive(list):

	list_full_tree = {}
	sections = Section.objects.filter(list=list.id)
	some_section = Section.objects.filter(list=list.id)[0]

	root_section = some_section.get_root()
	descendants_sections = root_section.get_descendants(include_self=True)

	list_full_tree['list'] = get_attr_as_dict(list)

	list_full_tree['list']['section'] = []

	# TODO: implement nested list for section structure

	for sec in descendants_sections:
		section_obj = get_attr_as_dict(sec)
		section_obj['pharmaceutical_forms'] = []

		section_pharm_forms = SectionPharmForm.objects.filter(section=sec.id)

		for ph_form in section_pharm_forms:
			ph_form_attrs = get_attr_as_dict(ph_form)
			section_obj['pharmaceutical_forms'].append(ph_form_attrs)
		
		list_full_tree['list']['section'].append(section_obj)

	list_tree_json = json.dumps(list_full_tree, indent=4, sort_keys=True)

	# Save history record
	history = History(
		name = list.name,
		year = list.year,
		type = list.type,
		subtype = list.subtype,
	)
	history.content = list_tree_json
	history.save()


def get_attr_as_dict(obj):
	dict = {}

	for attr in obj.__dict__:
		if not attr in ('id', '_state', 'created', '_mptt_cached_fields', 'rght', 'lft'):
			if not "_id" in attr:
				dict[attr] = obj.__dict__[attr]
			elif attr == 'pharmaceutical_form_id':
				ph_form = PharmaceuticalForm.objects.get(pk = obj.__dict__[attr])

				dict['pharmaceutical_form'] = {
					'name': ph_form.medicine.name, 
					'form': ph_form.pharmaceutical_form_type.name, 
					'composition':  ph_form.composition
				}

		
	return dict			
