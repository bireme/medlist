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

	ITEMS_PER_PAGE = 0

	output = {}

	lists_special = List.objects.filter(published=True).exclude(type='c')
	lists_country = List.objects.filter(published=True).filter(type='c')
	
	lists = []
	if 'lists' in request.GET and request.GET['lists'] != "":
		lists = request.GET['lists'].split(',')

	# if not load some lists, the section_form becomes empty
	section_forms = []
	if len(lists) > 0:
		section_forms = SectionPharmForm.objects.filter(section__list__id__in=lists).distinct()

	# removes all duplicated pharmaceutical form
	forms = []
	for sf in section_forms:
		id = sf.pharmaceutical_form.id
		if id in forms:
			section_forms = section_forms.exclude(pk=sf.id)
		else:
			forms.append(id)

	# make structure of comparation
	selected_lists = []
	for list in lists:
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
	
	# list only matcheds in all lists selecteds
	matcheds = {}
	for sf in section_forms:
		is_match = True
		for list in selected_lists:
			if not sf.pharmaceutical_form.id in list['forms']:
				is_match = False

		if is_match:
			matcheds[sf.pharmaceutical_form.id] = True
	
	matcheds = matcheds.keys()

	# if only matched selected	
	if 'only_matched' in request.GET and request.GET['only_matched'] == "true":		
		
		# filter the medicine that will be dislayed
		for sf in section_forms:
			if not sf.pharmaceutical_form.id in matcheds:
				section_forms = section_forms.exclude(pk=sf.id)

	# if only unmatched selected	
	if 'only_unmatched' in request.GET and request.GET['only_unmatched'] == "true":		
	
		# filter the medicine that will be dislayed
		for sf in section_forms:
			if sf.pharmaceutical_form.id in matcheds:
				section_forms = section_forms.exclude(pk=sf.id)		

	# pagination
	if ITEMS_PER_PAGE > 0:
		
		start = 0
		
		if 'page' in request.GET:
			page = int(request.GET['page'])
			start = (ITEMS_PER_PAGE * page) - ITEMS_PER_PAGE
		
		finish = start + ITEMS_PER_PAGE
		
		pagination = {}
		total_pages = len(section_forms) / ITEMS_PER_PAGE
		if (len(section_forms) % ITEMS_PER_PAGE) != 0:
			total_pages += 1
		pagination['items'] = range(1, total_pages+1)
		output['pagination'] = pagination

		section_forms = section_forms[start:finish]

	output['lists_special'] = lists_special
	output['lists_country'] = lists_country
	output['section_forms'] = section_forms
	output['selected_lists'] = selected_lists

	return render_to_response('list/compare.html', output, context_instance=RequestContext(request))
