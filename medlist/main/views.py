from django.shortcuts import render_to_response
from medlist.list.models import List
from django.template import RequestContext

def index(request):

	lists = List.objects.all().order_by("name")
	print lists
	paho_lists = lists.filter(type="p")
	who_lists = lists.filter(type="w")
	country_lists = lists.filter(type="c")

	dict_response = RequestContext (request, {
		'paho_lists' : paho_lists,
		"who_lists" : who_lists,
		"country_lists" : country_lists,
	})

	return render_to_response("main/index.html", dict_response)
