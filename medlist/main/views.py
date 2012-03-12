from django.shortcuts import render_to_response
from medlist.list.models import List
from django.template import RequestContext

def index(request):

	lists = List.objects.all()
	country = lists.filter(is_country=True)
	special = lists.filter(is_special=True)

	dict_response = RequestContext (request, {
		'lists_country': country,
		'lists_special': special,
	})

	return render_to_response("main/index.html", dict_response)
