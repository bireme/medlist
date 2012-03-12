#! coding:utf-8
from medlist.directory.models import *
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext

def show_medicine(request, id):
	
	# get the medicine 
	try:
		medicine = Medicine.objects.get(id=id)
	except:
		return HttpResponse("Medicamento não encontrado")

	# get pharm forms contents in this medicine
	pharm_forms = PharmaceuticalForm.objects.filter(medicine=id)

	new_forms = {}
	for form in pharm_forms:
		new_forms[form.id] = {}
		new_forms[form.id]['form'] = form

	dict_response = RequestContext (request, {
		'medicine': medicine,
		'pharm_forms': pharm_forms,
		'forms': new_forms,
	})

	return render_to_response('directory/show_medicine.html', dict_response, 
		context_instance=RequestContext(request))


