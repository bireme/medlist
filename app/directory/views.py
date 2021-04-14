#! coding:utf-8
from django.shortcuts import render, render_to_response, HttpResponse
from django.http import Http404
from django.template import RequestContext

from list.models import *
from evidence.models import MedicineEvidenceSummary
from directory.models import *

def show_medicine(request, id):

	# get the medicine
	try:
		medicine = Medicine.objects.get(id=id)
	except:
		raise Http404

	# get pharm forms contents in this medicine
	pharm_forms = PharmaceuticalForm.objects.filter(medicine=id)

	# get evidences summaries of medicine
	evidences = MedicineEvidenceSummary.objects.filter(medicine=id)

	# making lists
	forms_in_lists = {}
	for list in List.objects.filter(published=True):
		for form in pharm_forms:

			if not list.id in forms_in_lists.keys():
				forms_in_lists[list.id] = {'type': list.type, 'forms': [], 'list': List.objects.get(id=list.id)}

			if SectionPharmForm.objects.filter(section__list__id=list.id).filter(pharmaceutical_form=form):
				if not form.id in forms_in_lists[list.id]:
					forms_in_lists[list.id]["forms"].append(form.id)

	pharm_form_list = {}
	for form in pharm_forms:
		# get only pharmaceutical forms present in published lists
		form_in_lists = SectionPharmForm.objects.filter(pharmaceutical_form=form, section__list__published=True)
		if form_in_lists:
			pharm_form_list[form.id] = {}
			pharm_form_list[form.id]['form'] = form
			pharm_form_list[form.id]['form_pharmaceutical_form_type'] = form.pharmaceutical_form_type.get_translation(request.LANGUAGE_CODE)
			pharm_form_list[form.id]['form_in_lists'] = form_in_lists

	# sort list by pharmaceutical_form_type
	pharm_form_id_sorted = sorted(pharm_form_list, key=lambda x: pharm_form_list[x]['form_pharmaceutical_form_type'].lower())
	pharm_form_list_final = []
	for sorted_id in pharm_form_id_sorted:
		pharm_form_list_final.append(pharm_form_list[sorted_id])

	forms = []
	for form in pharm_forms:
		forms += SectionPharmForm.objects.filter(pharmaceutical_form=form, section__list__published=True)

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

	dict_response = {
		'medicine': medicine,
		'pharm_forms': pharm_forms,
		'pharm_form_list': pharm_form_list_final,
		'lists': lists,
		'countries': countries,
		'evidences': evidences,
		'forms_in_lists': forms_in_lists,
	}

	# if cames information
	if 'section' in request.GET:
		section = request.GET['section']

		section = Section.objects.get(pk=section)
		tree = section.get_ancestors()

		dict_response['section'] = section
		dict_response['tree'] = tree

	return render(request, 'directory/show_medicine.html', dict_response)
