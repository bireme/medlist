import json
from django.shortcuts import get_object_or_404, render_to_response, HttpResponse

from directory.models import *
from list.models import *


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

def get_pharmaceutical_forms(request):

	if 'ids' in request.GET and request.GET['ids'] != "":
		ids = request.GET['ids']
		ids = ids.split(",")

		output = {}
		for id in ids:
			try:
				obj = PharmaceuticalForm.objects.get(id=id)
				output[id]= "%s: %s" % (obj.id, obj.__unicode__())
			except: pass

		return HttpResponse(json.dumps(output), mimetype="application/json")

	all = PharmaceuticalForm.objects.all()
	if 'term' in request.GET and request.GET['term'] != "":
		all = all.filter(medicine__name__icontains=request.GET['term'])

	if 'id' in request.GET and request.GET['id'] != "":
		all = all.filter(id=request.GET['id'])

	output = []
	for item in all:
		# output.append({'id': item.id, 'name': item.__unicode__()})
		output.append("%s: %s" % (item.id, item.__unicode__()))

	return HttpResponse(json.dumps(output), mimetype="application/json")

def get_sections(request):

	output = {}
	if 'list' in request.GET and request.GET['list'] != "":
		list = request.GET['list']
		all = Section.objects.filter(list=list)

		for item in all:
			output[item.id] = item.__unicode__()

	return HttpResponse(json.dumps(output), mimetype="application/json")


def index(request):
	fator = 1
	from directory.app_actions import solr_index
	from datetime import datetime
	import time

	t1 = time.time()

	count = 1
	for medicine in Medicine.objects.all():

		solr_index(medicine)
		count += 1

	count = 1
	for section_pharm_form in SectionPharmForm.objects.all():

		section_pharm_form.save()
		count += 1

	t2 = time.time()
	ellapsed = t2-t1

	return HttpResponse("Ellapsed %fs" % ellapsed, mimetype="text/plain")
