#!coding: utf-8

from medlist.list.models import *
from django.shortcuts import HttpResponse, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404

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

	# just shows the list that not have been published yet if have 'preview' parameter
	if not list.published:
		# if not have preview parameter, returns 404 error
		if not 'preview' in request.GET.keys():
			raise Http404

	sections = Section.tree.filter(list=list)

	pharm_section = {}
	for section in sections:
		pharm_section[section.id] = SectionPharmForm.objects.filter(section=section)

	output = {'list': list}
	output['nodes'] = sections
	output['pharm_section'] = pharm_section
	
	return render_to_response('list/show_list.html', output, context_instance=RequestContext(request))

def compare(request):

	if not 'lists' in request.GET:
		lists = ''
	else:
		lists = request.GET['lists']

	output = {}

	lists_special = List.objects.filter(published=True).exclude(type='c')
	lists_country = List.objects.filter(published=True).filter(type='c')
	section_forms = SectionPharmForm.objects.all()

	selected_lists = []
	for list in lists.split(','):
		try:
			obj = List.objects.get(pk=list)
			tmp = {'obj': obj, 'forms': []}

			for sf in section_forms:
				if len(SectionPharmForm.objects
					.filter(section__list=obj)
					.filter(pharmaceutical_form=sf.pharmaceutical_form)) > 0:

					tmp['forms'].append(sf.pharmaceutical_form.id)

			selected_lists.append(tmp)
		except:
			pass
	
	output['lists_special'] = lists_special
	output['lists_country'] = lists_country
	output['section_forms'] = section_forms
	output['selected_lists'] = selected_lists

	return render_to_response('list/compare.html', output, context_instance=RequestContext(request))
