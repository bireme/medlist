# -*- coding: utf-8 -*-
from solr import SolrConnection
from django.conf import settings
from django.contrib import messages
from models import PharmaceuticalForm, MedicineLocal
from medlist.list.models import Section 


def solr_index(med):

	pharm_forms = med.pharmaceuticalform_set.all()
	form_cdata = []
	lists = []
	countries = []
	sections = []
	subsections = []

	med_local = MedicineLocal.objects.filter(medicine=med.id)
	medicine_names = ['en^%s' % med.name.strip()]
	for ml in med_local:
		medicine_names.append('%s^%s' % (ml.language, ml.name.strip()))

	for form in pharm_forms:
		form_cdata.append('type: "%s"; value: "%s"' % (form.pharmaceutical_form_type, form.composition))

	for form in pharm_forms:
		for section in Section.objects.filter(sectionpharmform=form):
			tree = section.get_ancestors()
			if tree:
				sections.append(tree[0].title)				
				for t in tree[1:]:
					subsections.append(t.title)
				subsections.append(section.title)
			else:
				sections.append(section.title)
				
			if section.list.type == 'c':
				countries.append(section.list.name)
			else:
				lists.append(section.list.abbreviation)

	# try to create a connection to a solr server and send medicine
	try:            
		solr = SolrConnection(settings.SOLR_URL)
		solr.add(
	    	id = str(med.id), 
	    	name = medicine_names,
	    	pharmaceutical_form = form_cdata,    	
	    	pharmaceutical_form_type = [form.pharmaceutical_form_type for form in pharm_forms],
	    	list=lists,
	    	country=countries,
	    	section=sections,
	    	subsection=subsections,
	    )
		response = solr.commit()
	except Exception as ex:	
		return False

	return True
