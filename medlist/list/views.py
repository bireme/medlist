#!coding: utf-8

from medlist.list.models import *
from django.shortcuts import HttpResponse, render_to_response, get_object_or_404
from django.template import RequestContext

def get_parents(id):
	output = {}
	for section in Section.objects.filter(parent=id):
		output[section.id] = {'title': section.title, 'parent': get_parents(section.id)}

	if output == {}:
		return 0
	else:
		return output

def show_list(request, id):

	list = get_object_or_404(List, pk=id)

	sections = Section.tree.all()

	pharm_section = {}
	for section in sections:
		pharm_section[section.id] = SectionPharmForm.objects.filter(section=section)

	output = {'list': list}
	output['nodes'] = sections
	output['pharm_section'] = pharm_section
	
	return render_to_response('list/show_list.html', output, context_instance=RequestContext(request))




