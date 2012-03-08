#!/usr/bin/env python
#!coding: utf-8

import json

output = {'docs': ""}

list = {
	'type': 'L',
	'name': 'WHO Model List of Essential Medicines',
	'abbreviation': 'EML',
	'is_country': False,
	'is_special_list': True,
	'year': 2011,
}

section = {
	'type': 'S',
	'name': 'ANAESTHETICS',
	'parent': False,
	'observation': None,
	'specialist_care': False,
	'complementary_list': False,
	'pharmaceuticalforms': [
		{
			"id": "medicine-pharmaceutical-form-id", # id vindo do direcotry do django
            "observation": None,
            "only_for_children": True,
            "square_box" : True,
            "specialist_care": True,
		},
	]
}

output['docs'] = [
	list,
	section,
]

print unicode(json.dumps(output, indent=4))