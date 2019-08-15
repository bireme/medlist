from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.conf import settings
from xml.etree import ElementTree

import requests
import json

@csrf_exempt
def get_scientific_production(request):
    text_param = request.GET.get('text')
    source_param = request.GET.get('source')
    service_url = "http://similardocs.bireme.org/SDService?adhocSimilarDocs={0}".format(text_param)
    if source_param:
        service_url = "{0}&sources={1}".format(service_url, source_param)

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


@csrf_exempt
def get_rxnorm_data(request):
    medicine_param = request.GET.get('medicine').strip()
    term_list = {}
    rxcui = ''

    rxnorm_api_url = 'https://rxnav.nlm.nih.gov/REST'
    find_url = "{0}/rxcui.json?name={1}".format(rxnorm_api_url, medicine_param)

    # Try to find medicine
    try:
        find_response = requests.get(find_url)
        find_json = find_response.json()

        # If found medicine retrieve Rx ID
        if 'idGroup' in find_json:
            if 'rxnormId' in find_json['idGroup']:
                rxcui =  find_json['idGroup']['rxnormId'][0]
    except:
        pass

    # With Rx Id consult additional data (Clinical Drug or Pack, etc)
    if rxcui != '':
        data_url = "{0}/rxcui/{1}/related.json?tty=SCD+SBD".format(rxnorm_api_url, rxcui)
        has_data = False
        try:
            data_response = requests.get(data_url)
            data_json = data_response.json()

            if data_json['relatedGroup']:
                concept_list = data_json['relatedGroup']['conceptGroup']
                for concept in concept_list:
                    tty = concept['tty']
                    term_list[tty] = []
                    for prop in concept['conceptProperties']:
                        has_data = True
                        term_list[tty].append({'name': prop['name'], 'id': prop['rxcui']})

                    term_list[tty] = sorted(term_list[tty], key = lambda i: i['name'])
        except:
            pass

        # if term_list has only parameter data delete it
        if not has_data:
            term_list = {}

    return render_to_response('utils/rxnorm_data.html',
                                        {'term_list': term_list, 'medicine': medicine_param})
