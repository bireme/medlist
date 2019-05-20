from django.shortcuts import render
from django.http import HttpResponse
from list.models import List


def index(request):

    lists = List.objects.all().order_by("name")
    paho_lists = lists.filter(type="p")
    who_lists = lists.filter(type="w")
    country_lists = lists.filter(type="c")

    dict_response = {'paho_lists' : paho_lists, 'who_lists' : who_lists, 'country_lists' : country_lists}

    return render(request, 'main/index.html', dict_response)


def close_window(request):
    output = "<html><head><script>window.parent.CloseModal();</script></head></html>"
    return HttpResponse(output)
