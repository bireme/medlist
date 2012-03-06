#! coding:utf-8
from medlist.directory.models import *
from django.shortcuts import render_to_response, HttpResponse

def show_medicine(request, id):
	
	# get the medicine 
	try:
		medicine = Medicine.objects.get(id=id)
	except:
		return HttpResponse("Medicamento não encontrado")

	# get pharm forms contents in this medicine
	pharm_forms = PharmaceuticalForm.objects.filter(medicine=id)

	# select all lists to compair
	all_lists = []
	for list in MedicineList.objects.all():
		all_lists.append(list)

	evidences = {}
	for form in pharm_forms:
		evidence = EvidenceSummary.objects.filter(pharmaceutical_form=form.id)
		if evidence.count() > 0:
			evidences[form.id] = evidence

	new_forms = {}
	for form in pharm_forms:
		new_forms[form.id] = {}
		new_forms[form.id]['form'] = form
		new_forms[form.id]['evidence'] = []
		for evidence in EvidenceSummary.objects.filter(pharmaceutical_form=form.id):
			tmp = {}
			tmp['evidence'] = evidence
			tmp['file'] = EvidenceSummaryUpload.objects.filter(evidence=evidence.id)

			new_forms[form.id]['evidence'].append(tmp)


	dict_response = {
		'medicine': medicine,
		'pharm_forms': pharm_forms,
		'all_lists': all_lists,
		'forms': new_forms,
	}

	return render_to_response('directory/show_medicine.html', dict_response)


