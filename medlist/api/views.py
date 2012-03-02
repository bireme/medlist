from medlist.directory.models import *
from django.shortcuts import get_object_or_404, render_to_response

def iahx(request):

	medicines = get_object_or_404(Medicine.objects.all())

	return render_to_response('api/iahx.xml', medicines)
