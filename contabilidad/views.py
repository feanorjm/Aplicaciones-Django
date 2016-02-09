import os
from datetime import date
from django.shortcuts import render_to_response
from django.db.models import Sum, Count, Avg
from contabilidad.models import Transacciones
from chartit import DataPool, Chart



def transacciones(request):
	listado_trans = Transacciones.objects.values('consumidor').annotate(monto_total=Sum('monto'))
	return render_to_response('listado_trans.html', {'listado_trans': listado_trans})



def chart_view(request):
    #Grafico 1
    data = \
        DataPool(
           series=
            [{'options': {
               'source': Transacciones.objects.values('consumidor').annotate(monto=Sum('monto'))},
              'terms': ['consumidor','monto']}
             ])

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

    #Grafico 2
    data2 = \
        DataPool(
           series=
            [{'options': {
               'source': Transacciones.objects.values('tipo_gasto').annotate(monto=Sum('monto'))},
              'terms': ['tipo_gasto','monto']}
             ])

    cht2 = Chart(
            datasource = data2,
            series_options =
              [{'options':{
                  'type': 'column',
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

    #Grafico 3
    data3 = \
        DataPool(
           series=
            [{'options': {
               'source': Transacciones.objects.values('consumidor','monto').filter(tipo_gasto='TELEFONO')}, #fecha__month=date.today().month)},
              'terms': ['consumidor','monto']}
             ])

    cht3 = Chart(
            datasource = data3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'stacking': False},
                'terms':{
                  'consumidor': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Gasto en telefono por Persona'},
               'xAxis': {
                    'title': {
                       'text': 'Consumidor'}}})

    #Grafico 4
    data4 = \
        DataPool(
           series=
            [{'options': {
               'source': Transacciones.objects.values('consumidor','monto').filter(tipo_gasto='COMBUSTIBLE')}, #,fecha__month=date.today().month)},
              'terms': ['consumidor','monto']}
             ])

    cht4 = Chart(
            datasource = data4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'stacking': False},
                'terms':{
                  'consumidor': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Gasto en combustible por Persona'},
               'xAxis': {
                    'title': {
                       'text': 'Consumidor'}}})



    #Step 3: Send the chart object to the template.
    return render_to_response('chart1.html',{'weatherchart': [cht,cht2,cht3,cht4],})


