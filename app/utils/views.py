from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.conf import settings
from xml.etree import ElementTree

import requests

# Create your views here.
@csrf_exempt
def get_scientific_production(request):
    text_param = request.GET.get('text')
    service_url = "{0}?adhocSimilarDocs={1}".format(settings.VHL_SIMILAR_SERVICE_URL, text_param)

    response = requests.get(service_url)

    reference_list = []
    root = ElementTree.fromstring(response.content)

    for doc in root.iter('document'):
        doc_elements = doc.getchildren()
        ref = {}
        for element in doc_elements:
            ref[element.tag] = element.text

        reference_list.append(ref)

    return render_to_response('utils/scientific_production.html',
                                                {'reference_list': reference_list})
