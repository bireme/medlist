from medlist.directory.models import *
from medlist.list.models import *
from django.shortcuts import get_object_or_404, render_to_response, HttpResponse
import json

# dict that has the id-section relation
id_section = {}

def get_depth(id, depth_number=0):
	"""
		Function that makes a recursive search in models to
		construct the dict which have id-section relation
	"""
	global id_section

	output = {}
	count = 1
	obj = Section.objects.get(id=id)

	for section in Section.objects.filter(parent=id):
		if depth_number == 0:
			hierarchy_number = count
		else:
			hierarchy_number = "%s.%s" % (depth_number, count)

		id_section[section.id] = hierarchy_number
		
		output[section.id] = {'children': get_depth(section.id, hierarchy_number), 'title': section.title, 'hierarchy_number': hierarchy_number}
		count += 1

	if output == {}:
		return None
	else:
		return output

def get_hierarchy_relation(request, list):

	global id_section

	sections = {}
	count = 1

	obj_sections = Section.objects.filter(list=list)
	obj_sections = obj_sections.filter(parent=None)
	
	for section in obj_sections:
		id_section[section.id] = unicode(count)
		sections[section.id] = {'children': get_depth(section.id, count), 'title': section.title, 'hierarchy_number': count}
		count += 1

	return HttpResponse(json.dumps(id_section))


def iahx(request):

	try:
		medicines = Medicine.objects.all()
	except:
		return HttpResponse("Erro: Nenhum objeto foi encontrado")

	output = []
	for med in medicines:
		
		forms = PharmaceuticalForm.objects.filter(medicine=med.id)
		med_local = MedicineLocal.objects.filter(medicine=med.id)

		tmp = {}
		tmp['medicine'] = med
		tmp['forms'] = forms
		tmp['local'] = med_local

		output.append(tmp)

	return render_to_response('api/iahx.xml', {'medicines': output}, mimetype="Content-type: text/xml")

def get_section_parents(request, id_section):

	output = {'id': id_section}
	output['parents'] = []
	for section in Section.objects.filter(parent=id_section):
		current = {'id': section.id, 'title': section.title}
		output['parents'].append(current)

	return HttpResponse(json.dumps(output), mimetype="application/json")


