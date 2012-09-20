from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *

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

	return render_to_response("evidence/show.html", output, context_instance=RequestContext(request))
