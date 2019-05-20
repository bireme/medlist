from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from evidence.models import *

def show(request, id):
    output = {}
    evidence = None
    language = request.LANGUAGE_CODE

    evidence_summary = get_object_or_404(EvidenceSummary, pk=id)
    evidence_local = EvidenceSummaryLocal.objects.filter(evidence=evidence_summary).filter(language=language)

    if evidence_local:
        evidence = evidence_local[0]
    else:
        evidence = evidence_summary

    output['evidence'] = evidence

    return render(request, 'evidence/show.html', output)
