#!coding: utf-8

from medlist.list.models import *
from django.shortcuts import HttpResponse, render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from django.http import Http404
import settings

def get_parents(id):
	output = {}
	for section in Section.objects.filter(parent=id):
		output[section.id] = {'title': section.title, 'parent': get_parents(section.id)}

	if output == {}:
		return 0
	else:
		return output

@cache_page(settings.SHOW_LIST_CACHE)
def show_list(request, id):

	list = get_object_or_404(List, pk=id)

	# just shows the list that not have been published yet if have 'preview' parameter
	if not list.published:
		# if not have preview parameter, returns 404 error
		if not 'preview' in request.GET.keys():
			raise Http404

	sections = Section.tree.filter(list=list)
	sections_has_complementary = []
	for section in sections:
		if SectionPharmForm.objects.filter(section=section).filter(complementary_list=True).count() > 0:
			sections_has_complementary.append(section.id)


	pharm_section = {}
	for section in sections:
		query = SectionPharmForm.objects.filter(section=section)
		pharm_section[section.id] = query
		

	output = {'list': list}
	output['nodes'] = sections
	output['pharm_section'] = pharm_section
	output['sections_has_complementary'] = sections_has_complementary
	
	return render_to_response('list/show_list.html', output, context_instance=RequestContext(request))

#@cache_page(settings.SHOW_LIST_CACHE)
def compare(request):

	output = {}

	lists_special = List.objects.filter(published=True).exclude(type='c')
	lists_country = List.objects.filter(published=True).filter(type='c')

	lists = []
	if 'lists' in request.GET and request.GET['lists'] != "":
		lists = request.GET['lists'].split(',')
		if 'null' in lists:
			lists.remove("null")

	# if not load some lists, the section_form becomes empty
	section_forms = []
	if len(lists) > 0:
		section_forms = SectionPharmForm.objects.filter(section__list__id__in=lists).distinct()

	# removes all duplicated pharmaceutical form
	# forms = []
	# for sf in section_forms:
	# 	id = sf.pharmaceutical_form.id
	# 	if id in forms:
	# 		section_forms = section_forms.exclude(pk=sf.id)
	# 	else:
	# 		forms.append(id)

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
	if 'items_per_page' in request.GET and request.GET['items_per_page'] > -1:
		ITEMS_PER_PAGE = int(request.GET['items_per_page'])
	else:
		ITEMS_PER_PAGE = settings.ITEMS_PER_PAGE

	if ITEMS_PER_PAGE > 0:
		
		pagination = {}
		start = 0
		
		total_pages = len(section_forms) / ITEMS_PER_PAGE
		if (len(section_forms) % ITEMS_PER_PAGE) != 0:
			total_pages += 1

		pagination['items'] = range(1, total_pages+1)
		
		if 'page' in request.GET and request.GET['page'] > 0:
			try:
				page = int(request.GET['page'])
			except:
				page = 1
			
			start = (ITEMS_PER_PAGE * page) - ITEMS_PER_PAGE
		
			if page > 1:
				pagination['prev'] = page - 1

			if page < total_pages:
				pagination['next'] = page + 1

			pagination['page'] = page
		else:
			pagination['page'] = 1			
			pagination['next'] = 2
		
		finish = start + ITEMS_PER_PAGE
		
		output['pagination'] = pagination

		section_forms = section_forms[start:finish]

	output['lists_special'] = lists_special
	output['lists_country'] = lists_country
	output['section_forms'] = section_forms
	output['selected_lists'] = selected_lists

	return render_to_response('list/compare.html', output, context_instance=RequestContext(request))
