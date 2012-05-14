#!coding: utf-8

from medlist.list.models import *
from django.shortcuts import HttpResponse, render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.http import Http404
from django.core.cache import cache
from search import search
import settings

def get_parents(id):
	output = {}
	for section in Section.objects.filter(parent=id):
		output[section.id] = {'title': section.title, 'parent': get_parents(section.id)}

	if output == {}:
		return 0
	else:
		return output

@cache_page(settings.CACHE_TIMEOUT)
@csrf_protect
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

#@cache_page(settings.CACHE_TIMEOUT)
def compare(request):

	output = {}

	# output lists to make form
	output['lists_special'] = List.objects.filter(published=True).exclude(type='c')
	output['lists_country'] = List.objects.filter(published=True).filter(type='c')

	list_of_lists = []
	if 'lists' in request.GET and request.GET['lists'] != "":
		# remove nulls from list
		lists = request.GET['lists'].replace(',null', '').replace('null', '')
		# make a list of the lists
		list_of_lists = lists.split(',')
		# Make a OR query to get all forms in these lists
		lists = lists.replace(",", " OR ")
	else:
		lists = ""

	# if MATCHEDS, make a AND query
	if request.GET.get('only_matched') and request.GET.get('only_matched') == 'true':
		lists = lists.replace("OR", "AND")

	# if UNMATCHEDS, make a ANDNOT query
	elif request.GET.get('only_unmatched') and request.GET.get('only_unmatched') == 'true':
		lists = lists.replace("OR", "ANDNOT")
	
	# search these forms
	pharmaceutical_forms = search(lists)
	print len(pharmaceutical_forms)

	languages = {}
	languages['pt-br'] = ['medicine_pt', 'type_pt']
	languages['es'] = ['medicine_es', 'type_es']

	if request.LANGUAGE_CODE != 'en':
		count = 0
		for form in pharmaceutical_forms:
			for lang in languages[request.LANGUAGE_CODE]:
				if lang in form and form[lang]:
					field = lang.split("_")[0]
					form[field] = form[lang]

			pharmaceutical_forms[count] = form
			count += 1
	
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
	output['lists'] = List.objects.filter(id__in=list_of_lists)
	output['paginator'] = paginator
	output['pagination'] = pagination

	return render_to_response('list/compare.html', output, context_instance=RequestContext(request))
