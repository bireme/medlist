# -*- coding: utf-8 -*-
from solr import SolrConnection
from django.conf import settings
from django.contrib import messages
from models import PharmaceuticalForm, PharmaceuticalFormTypeLocal, MedicineLocal
from medlist.list.models import Section, SectionPharmForm
from medlist.evidence.models import MedicineEvidenceSummary


def solr_index(med):
    lists = []
    countries = []
    sections = []
    subsections = []
    pharma_form_list = []
    pharma_form_type_list = []
    category_list = []
    observation_list = []

    # if medicine status is not active delete from solr index
    if not med.active:
        try:
            solr = SolrConnection(settings.SOLR_URL)
            solr.delete(id=str(med.id))
            response = solr.commit()
        except Exception as ex: 
            return False

        return True

    # index medicine on solr index
    medicine_translations = MedicineLocal.objects.filter(medicine=med.id)
    medicine_list = ['en^%s' % med.name.strip()]
    for translation in medicine_translations:
        medicine_list.append('%s^%s' % (translation.language, translation.name.strip()))
    
    medicine_list = "|".join(medicine_list) # ex.: en^codeine|pt-br^codeína|es^codeína

    # retrieve actives pharmaceutical forms of currente medicine
    pharm_forms = med.pharmaceuticalform_set.filter(active=True)
    for form in pharm_forms:

        # ex. ^enTablet|es^Tableta|pt-br^Comprimido
        pharma_form_type_translations = "|".join( form.pharmaceutical_form_type.get_translations() )
        pharma_form_type_list.append(pharma_form_type_translations)

        # ex. ^enTablet|es^Tableta|pt-br^Comprimido|comp^15 mg/ml
        pharma_form_list.append('%s|comp^%s' % (pharma_form_type_translations, form.composition))

        # create category_list (section and subsection where current pharmaceutical form is used on lists)
        section_pharm_form_list = SectionPharmForm.objects.filter(pharmaceutical_form=form)

        for section_pharm_form in section_pharm_form_list:
            #add observations of current section_pharm_form
            if section_pharm_form.only_for_children:
                observation_list.append('only_for_children')
            if section_pharm_form.specialist_care_for_children:
                observation_list.append('specialist_care_for_children')
            if section_pharm_form.restriction_age:
                observation_list.append('restriction_age')
            if section_pharm_form.best_evidence:
                observation_list.append('best_evidence')
            if section_pharm_form.observation:
                observation_list.append('observation')

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

    #check if current medicine have Evidence summaries
    has_evidence = ""
    evidence_total = MedicineEvidenceSummary.objects.filter(medicine=med.id).count()
    if evidence_total > 0:
        has_evidence = "true"

    # try to create a connection to a solr server and send medicine
    try:
        solr = SolrConnection(settings.SOLR_URL)
        solr.add(
            id = str(med.id), 
            type = "medicine",
            name = medicine_list,
            pharmaceutical_form = pharma_form_list,        
            pharmaceutical_form_type = pharma_form_type_list,
            list=lists,
            country=countries,
            category=category_list,
            observation=observation_list,
            has_evidence=has_evidence,
        )
        response = solr.commit()
    except Exception as ex: 
        return False

    return True

