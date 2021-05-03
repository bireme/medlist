#!coding: utf-8

from django.shortcuts import HttpResponse, render, render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.http import Http404
from django.core.cache import cache
from utils.decorators import conditional_cache

from list.models import *
from list.search import search
from history.models import *

from medlist import settings

def get_parents(id):
	output = {}
	for section in Section.objects.filter(parent=id):
		output[section.id] = {'title': section.title, 'parent': get_parents(section.id)}

	if output == {}:
		return 0
	else:
		return output

@conditional_cache(decorator=cache_page(settings.CACHE_TIMEOUT))
@csrf_protect
def show_list(request, id):

	list = get_object_or_404(List, pk=id)

	# just shows the list that not have been published yet if have 'preview' parameter
	if not list.published:
		# if not have preview parameter, returns 404 error
		if not 'preview' in request.GET.keys():
			raise Http404

	sections = Section.objects.filter(list=list)
	sections_has_complementary = []
	for section in sections:
		if SectionPharmForm.objects.filter(section=section).filter(complementary_list=True).count() > 0:
			sections_has_complementary.append(section.id)


	pharm_section = {}
	for section in sections:
		query = SectionPharmForm.objects.filter(section=section).order_by('pharmaceutical_form__medicine__name')
		pharm_section[section.id] = query

	history_list = History.objects.filter(abbreviation=list.abbreviation)

	output = {'list': list}
	output['nodes'] = sections
	output['pharm_section'] = pharm_section
	output['sections_has_complementary'] = sections_has_complementary
	output['history_list'] = history_list

	return render(request, 'list/show_list.html', output)

#@conditional_cache(decorator=cache_page(settings.CACHE_TIMEOUT))
def compare(request):

	output = {}

	# output lists to make form
	output['lists_special'] = List.objects.filter(published=True).exclude(type='c')
	output['lists_country'] = List.objects.filter(published=True).filter(type='c').order_by('name')

	list_of_lists = []

	list_param = request.GET.getlist('list')
	comparative_type_param = request.GET.get('comparative_type', 'complete')
	matches_param = request.GET.get('matches', 'all')

	lists = ' OR '.join(list_param)

	# if MATCHEDS, make a AND query
	if matches_param == 'only_matched':
		lists = lists.replace("OR", "AND")

	# if UNMATCHEDS, make a ANDNOT query
	elif matches_param == 'only_unmatched':
		lists = "(%s) ANDNOT (%s)" % (lists, lists.replace("OR", "AND"))

	# search these forms
	search_result = search(lists, filter_compare=comparative_type_param)

	# sort by medicine name
	sort_by_field_name = 'medicine'
	if request.LANGUAGE_CODE != 'en':
		if request.LANGUAGE_CODE == 'es':
			sort_by_field_name = 'medicine_es'
		else:
			sort_by_field_name = 'medicine_pt'

	pharmaceutical_forms = sorted(search_result, key=lambda x: x[sort_by_field_name].lower())

	# make pagination
	paginator = Paginator(pharmaceutical_forms, settings.ITEMS_PER_PAGE)
	if request.GET.get('page'):
		page = request.GET.get('page')
		try: pagination = paginator.page(page)
		except EmptyPage: pagination = paginator.page(paginator.num_pages)
	else:
		pagination = paginator.page(1)

	# output all results
	output['pharmaceutical_forms'] = pagination.object_list
	output['lists'] = List.objects.filter(id__in=list_param)
	output['paginator'] = paginator
	output['pagination'] = pagination
	output['list_param'] = list_param
	output['comparative_type_param'] = comparative_type_param
	output['matches_param'] = matches_param

	return render(request, 'list/compare.html', output)
