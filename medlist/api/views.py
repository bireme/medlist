from medlist.directory.models import *
from django.shortcuts import get_object_or_404, render_to_response, HttpResponse

def iahx(request):

	try:
		medicines = Medicine.objects.all()
	except:
		return HttpResponse("Erro: Nenhum objeto foi encontrado")

	output = []
	for med in medicines:
		
		forms = PharmaceuticalForm.objects.filter(medicine=med.id)
		med_local = MedicineLocal.objects.filter(medicine=med.id)

		tmp = {}
		tmp['medicine'] = med
		tmp['forms'] = forms
		tmp['local'] = med_local

		output.append(tmp)

	return render_to_response('api/iahx.xml', {'medicines': output}, mimetype="Content-type: text/xml")
