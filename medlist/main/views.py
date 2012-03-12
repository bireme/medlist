from django.shortcuts import render_to_response
from medlist.list.models import List

def index(request):

	lists = List.objects.all()
	country = lists.filter(is_country=True)
	special = lists.filter(is_special=True)

	dict_response = {
		'lists_country': country,
		'lists_special': special,
	}

	return render_to_response("main/index.html", dict_response)
