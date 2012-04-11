# -*- coding: utf-8 -*-
from solr import SolrConnection
from django.conf import settings
from django.contrib import messages
from models import PharmaceuticalForm, PharmaceuticalFormTypeLocal, MedicineLocal
from medlist.list.models import Section, SectionPharmForm


def solr_index(med):
    lists = []
    countries = []
    sections = []
    subsections = []
    pharma_form_list = []
    pharma_form_type_list = []
    category_list = []

    # medicine
    medicine_translations = MedicineLocal.objects.filter(medicine=med.id)
    medicine_list = ['en^%s' % med.name.strip()]
    for translation in medicine_translations:
        medicine_list.append('%s^%s' % (translation.language, translation.name.strip()))
    
    medicine_list = "|".join(medicine_list) # ex.: en^codeine|pt-br^codeína|es^codeína

    # pharmaceutical forms
    pharm_forms = med.pharmaceuticalform_set.all()
    for form in pharm_forms:

        # ex. ^enTablet|es^Tableta|pt-br^Comprimido
        pharma_form_type_translations = "|".join( form.pharmaceutical_form_type.get_translations() )
        pharma_form_type_list.append(pharma_form_type_translations)

        # ex. ^enTablet|es^Tableta|pt-br^Comprimido|comp^15 mg/ml
        pharma_form_list.append('%s|comp^%s' % (pharma_form_type_translations, form.composition))

        # create category_list (section and subsection where current pharmaceutical form is used on lists)
        section_pharm_form_list = SectionPharmForm.objects.filter(pharmaceutical_form=form)

        for section_pharm_form in section_pharm_form_list:
            section = Section.objects.get(pk=section_pharm_form.section.id)
            section_translations = "|".join(section.get_translations())

            section_tree = section.get_ancestors()
            
            if section_tree:
                for sec in section_tree:                    
                    category_translations = "|".join(sec.get_translations())
                    if category_translations not in category_list:
                        category_list.append(category_translations)
            
            if section_translations not in category_list:
                category_list.append(section_translations)
   
            list_associated = "|".join( section.list.get_translations() )
            if section.list.type == 'c':                                
                countries.append( list_associated)
            else:                
                if list_associated not in lists:
                    lists.append( list_associated )


    # try to create a connection to a solr server and send medicine
    try:
        solr = SolrConnection(settings.SOLR_URL)
        solr.add(
            id = str(med.id), 
            name = medicine_list,
            pharmaceutical_form = pharma_form_list,        
            pharmaceutical_form_type = pharma_form_type_list,
            list=lists,
            country=countries,
            category=category_list,
        )
        response = solr.commit()
    except Exception as ex: 
        return False

    return True

