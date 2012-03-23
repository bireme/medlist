#! coding:utf-8
from medlist.directory.models import *
from django.shortcuts import render_to_response, HttpResponse
from django.http import Http404
from django.template import RequestContext
from medlist.list.models import *

def show_medicine(request, id):
	
	# get the medicine 
	try:
		medicine = Medicine.objects.get(id=id)
	except:
		raise Http404

	# get pharm forms contents in this medicine
	pharm_forms = PharmaceuticalForm.objects.filter(medicine=id)

	# get evidences summaries of medicine
	evidences = medicine.evidencesummary_set.all()

	# making lists
	forms_in_lists = {}
	for list in List.objects.filter(published=True):
		for form in pharm_forms:
			
			if not list.abbreviation in forms_in_lists.keys():
				forms_in_lists[list.abbreviation] = {'type': list.type, 'forms': []}
			
			if SectionPharmForm.objects.filter(section__list__id=list.id).filter(pharmaceutical_form=form): 
				if not form.id in forms_in_lists[list.abbreviation]:
					forms_in_lists[list.abbreviation]["forms"].append(form.id)			

	new_forms = {}
	for form in pharm_forms:
		new_forms[form.id] = {}
		new_forms[form.id]['form'] = form

	forms = []
	for form in pharm_forms:
		forms += SectionPharmForm.objects.filter(pharmaceutical_form=form)

	tmp_lists = {}
	tmp_countries = {}
	for form in forms:
		for section in Section.objects.filter(sectionpharmform=form):
			if section.list.type == 'c':
				tmp_countries[section.list.name] = True
			else:
				tmp_lists[section.list.subtype] = True
							

	lists = tmp_lists.keys()
	countries = tmp_countries.keys()

	dict_response = RequestContext (request, {
		'medicine': medicine,
		'pharm_forms': pharm_forms,
		'forms': new_forms,
		'lists': lists,
		'countries': countries,
		'evidences': evidences,
		'forms_in_lists': forms_in_lists,
	})

	# if cames information
	if 'section' in request.GET:
		section = request.GET['section']

		section = Section.objects.get(pk=section)
		tree = section.get_ancestors()

		dict_response['section'] = section
		dict_response['tree'] = tree

	return render_to_response('directory/show_medicine.html', dict_response, 
		context_instance=RequestContext(request))


