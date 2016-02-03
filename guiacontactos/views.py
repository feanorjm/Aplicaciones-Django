from django.shortcuts import render_to_response
from guiacontactos.models import Personas

def personas(request):
	lista = Personas.objects.all()
	return render_to_response('lista.html', {'lista': lista})

