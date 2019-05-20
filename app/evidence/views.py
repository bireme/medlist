from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from evidence.models import *

def show(request, id):

	output = {}
	language = request.LANGUAGE_CODE

	evidence = get_object_or_404(EvidenceSummary, pk=id)
	translate = EvidenceSummaryLocal.objects.filter(evidence=evidence).filter(language=language)

	if translate:
		translate = translate[0]
	else:
		translate = evidence

	output['evidence'] = evidence
	output['translate'] = translate

	return render(request, 'evidence/show.html', output)
