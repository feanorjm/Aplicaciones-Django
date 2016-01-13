from django.shortcuts import render_to_response
from contabilidad.models import Transacciones

def transacciones(request):
	listado_trans = Transacciones.objects.all()

	return render_to_response('listado_trans.html', {'listado_trans': listado_trans})