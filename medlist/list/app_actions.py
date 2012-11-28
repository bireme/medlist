# -*- coding: utf-8 -*-
import json
from django.conf import settings
from django.core import serializers
from django.contrib import messages
from django.template.loader import render_to_string
from django.template import RequestContext
from medlist.directory.models import PharmaceuticalForm, MedicineLocal
from medlist.list.models import List, ListLocal, Section, SectionPharmForm
from medlist.history.models import History, HistoryLocal
from datetime import datetime
import xml.dom.minidom


def create_list_archive(list):

    request = {}
    request['LANGUAGE_CODE'] = 'en'

    sections = Section.tree.filter(list=list)
    sections_has_complementary = []
    for section in sections:
        if SectionPharmForm.objects.filter(section=section).filter(complementary_list=True).count() > 0:
            sections_has_complementary.append(section.id)

    pharm_section = {}
    for section in sections:
        query = SectionPharmForm.objects.filter(section=section)
        pharm_section[section.id] = query
        

    output = {'list': list}
    output['nodes'] = sections
    output['pharm_section'] = pharm_section
    output['sections_has_complementary'] = sections_has_complementary
    output['request'] = request
    
    list_xml = render_to_string('history/xml_list.tpl', output)
    list_xml = list_xml.strip()

    list_html = render_to_string('history/show_list.html', output)
    list_html = list_html.strip()

    history = History(name=list.name, abbreviation=list.abbreviation, year=list.year, edition=list.edition, 
        type=list.type, subtype=list.subtype, published=list.published, obs=list.obs, created=datetime.now())
    
    history.content = list_html
    history.xml = list_xml

    # save history main 
    history.save()

    # save history translations
    save_translated_list_archive(list, history, output, request, 'pt-br')
    save_translated_list_archive(list, history, output, request, 'es')


def save_translated_list_archive(list, history, output, request, lang):

    request['LANGUAGE_CODE'] = lang
    output['request'] = request
    
    list_xml = render_to_string('history/xml_list.tpl', output)
    list_xml = list_xml.strip()

    list_html = render_to_string('history/show_list.html', output)
    list_html = list_html.strip()
   
    history_local = HistoryLocal(history=history, language=lang, name=list.get_translation(lang), obs=list.get_translation(lang + '|obs') )

    history_local.content = list_html
    history_local.xml = list_xml
    
    history_local.save()


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
