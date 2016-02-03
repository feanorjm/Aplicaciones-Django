import os
from django.shortcuts import render_to_response
from django.db.models import Sum, Count, Avg
from contabilidad.models import Transacciones
from chartit import DataPool, Chart



def transacciones(request):
	listado_trans = Transacciones.objects.values('consumidor').annotate(monto_total=Sum('monto'))
	return render_to_response('listado_trans.html', {'listado_trans': listado_trans})



def chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    data = \
        DataPool(
           series=
            [{'options': {
               'source': Transacciones.objects.values('consumidor').annotate(monto=Sum('monto'))},
              'terms': ['consumidor','monto']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = data,
            series_options =
              [{'options':{
                  'type': 'bar',
                  'stacking': False},
                'terms':{
                  'consumidor': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Total por consumidor'},
               'xAxis': {
                    'title': {
                       'text': 'Consumidor'}}})

    #Step 1: Create a DataPool with the data we want to retrieve.
    data2 = \
        DataPool(
           series=
            [{'options': {
               'source': Transacciones.objects.values('tipo_gasto').annotate(monto=Sum('monto'))},
              'terms': ['tipo_gasto','monto']}
             ])

    #Step 2: Create the Chart object
    cht2 = Chart(
            datasource = data2,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'stacking': False},
                'terms':{
                  'tipo_gasto': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Total por tipos de gastos'},
               'xAxis': {
                    'title': {
                       'text': 'Consumidor'}}})



    #Step 3: Send the chart object to the template.
    return render_to_response('chart1.html',{'weatherchart': [cht,cht2],})


