import os
from datetime import date, timedelta
from django.db import connection
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaccion, Consumidor, Nombre_entrada
from .forms import TransaccionForm
from chartit import DataPool, Chart
from django.contrib.auth.models import User



@login_required
def index_view(request):
    #listado_trans = Transacciones.objects.all().filter(fecha__month=date.today().month)
    total_gastos_mes = Transaccion.objects.filter(tipo_transaccion=2,fecha__month=3).aggregate(monto_total=Sum('monto'))['monto_total']
    #total_gastos_mes_ant = Transaccion.objects.filter(tipo_transaccion=2,fecha__month=2).aggregate(monto_total=Sum('monto'))['monto_total']
    porcentaje_mes_ant = 100
    total_gastos_global = Transaccion.objects.filter(tipo_transaccion=2).aggregate(monto_total=Sum('monto'))['monto_total']
    total_ingresos_global = Transaccion.objects.filter(tipo_transaccion=1).aggregate(monto_total=Sum('monto'))['monto_total']
    saldo_total = total_ingresos_global - total_gastos_global
    print(total_ingresos_global)

    #Grafico 0
    get_mes = connection.ops.date_trunc_sql('month', 'fecha')
    query = Transaccion.objects.filter(fecha__year=2016).extra({'fecha': get_mes})
    dinicio= query.values('consumidor__name','fecha').filter(tipo_transaccion=2).annotate(monto=Sum('monto')).order_by('fecha')
    meses = []
    consum = []
    datos = []
    for a in dinicio:
        data_inicial = [int(a['fecha'][5:7]),a['consumidor__name'],a['monto']]
        datos.append(data_inicial)
        mes = int(a['fecha'][5:7])
        consu = a['consumidor__name']
        if (mes in meses) == False:
            meses.append(mes)
        if (consu in consum) == False:
            consum.append(consu)

    print(datos)
    cht_index = []
    list = []
    for c in consum:
        data = []
        for mes in meses:
            last = 0
            for d in datos:
                if (mes == d[0]) & (c == d[1]):
                    data.append(d[2])
                    last = mes
                elif (c == d[1]) & (last == (mes -1)):
                    data.append(0)

        list.append(data)
    cht_index.append(meses)
    cht_index.append(consum)
    cht_index.append(list)

    def monthname(month_num):
        names ={'2016-01-01': 'Enero', '2016-02-01': 'Febrero', '2016-03-01': 'Marzo', '2016-04-01': 'Abril', '2016-05-01': 'Mayo', '2016-06-01': 'Junio',
        '2016-07-01': 'Julio', '2016-08-01': 'Agosto', '2016-09-01': 'Septiembre', '2016-10-01': 'Octubre', '2016-11-01': 'Noviembre', '2016-12-01': 'Diciembre'}
        return names[month_num]

    #Grafico 5 ingresos mensuales 2016
    get_mes = connection.ops.date_trunc_sql('month', 'fecha')
    query= Transaccion.objects.filter(fecha__year=2016,tipo_transaccion=1).extra({'fecha': get_mes})
    dinicio= query.values('fecha').annotate(monto=Sum('monto')).order_by('fecha')

    #print(dlist)
    data5 = \
        DataPool(
           series=
            [{'options': {
               'source': dinicio},
              'terms': ['fecha','monto']}
             ])
    cht5 = Chart(
            datasource = data5,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }
              },
                'terms':{
                  'fecha': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'INGRESOS MENSUALES AÑO 2016'},
                   'xAxis': {
                        'title': {
                            'text': 'MES'
                        }
                   }
              },
            x_sortf_mapf_mts = (None, monthname, False))

    #Step 3: Send the chart object to the template.

    return render_to_response('production/index.html',
                              {'total_gg': total_gastos_global,
                               'total_gm': total_gastos_mes,
                               'saldo_total': saldo_total,
                               'porcentaje': porcentaje_mes_ant,
                               'total_ig': total_ingresos_global,
                               'cht_index': cht_index,
                               'chartit_index': [cht5,]
                               },context_instance=RequestContext(request))


@login_required
def transacciones(request):
    #listado_trans = Transacciones.objects.all().filter(fecha__month=date.today().month)
    listado_trans = Transaccion.objects.filter(fecha__gt=date.today() - timedelta(2*365/12)).order_by('-fecha')#[:300]
    listado_trans = Transaccion.objects.all().order_by('-fecha')[:300]
    #total_trans = Transacciones.objects.filter(fecha__month=date.today().month).aggregate(monto_total=Sum('monto'))['monto_total']
    #return render_to_response('pagina_listado.html', {'listado_trans': listado_trans,'total': str(total_trans)})
    total_gastos_mes = Transaccion.objects.filter(tipo_transaccion=2,fecha__month=date.today().month-1).aggregate(monto_total=Sum('monto'))['monto_total']
    porcentaje_mes_ant = 100
    total_gastos_global = Transaccion.objects.filter(tipo_transaccion=2).aggregate(monto_total=Sum('monto'))['monto_total']
    total_ingresos_global = Transaccion.objects.filter(tipo_transaccion=1).aggregate(monto_total=Sum('monto'))['monto_total']
    saldo_total = total_ingresos_global - total_gastos_global

    users = Consumidor.objects.all()
    entradas = Nombre_entrada.objects.all()

    return render_to_response('production/tables_dynamic2.html',
                              {'listado_trans': listado_trans,
                               'total_gg': total_gastos_global,
                               'total_gm': total_gastos_mes,
                               'saldo_total': saldo_total,
                               'porcentaje': porcentaje_mes_ant,
                               'total_ig': total_ingresos_global,
                               'users': users,
                               'entradas':entradas,
                               },context_instance=RequestContext(request))


@login_required
def chart_view(request):
    #Grafico 0
    get_mes = connection.ops.date_trunc_sql('month', 'fecha')
    query= Transaccion.objects.filter(fecha__year=2016).extra({'fecha': get_mes})
    dinicio= query.values('consumidor__name','fecha').filter(tipo_transaccion=2).annotate(monto=Sum('monto')).order_by('fecha')
    meses = []
    consum = []
    datos = []
    for a in dinicio:
        data_inicial = [int(a['fecha'][5:7]),a['consumidor__name'],a['monto']]
        datos.append(data_inicial)
        mes = int(a['fecha'][5:7])
        consu = a['consumidor__name']
        if (mes in meses) == False:
            meses.append(mes)
        if (consu in consum) == False:
            consum.append(consu)

    grafico = []
    list = []
    for c in consum:
        data = []
        for mes in meses:
            last = 0
            for d in datos:
                if (mes == d[0]) & (c == d[1]):
                    data.append(d[2])
                    last = mes
                elif (c == d[1]) & (last == (mes -1)):
                    data.append(0)

        list.append(data)
    grafico.append(meses)
    grafico.append(consum)
    grafico.append(list)


    #Grafico 1
    get_mes = connection.ops.date_trunc_sql('month', 'fecha')
    query= Transaccion.objects.filter(fecha__year=2016,tipo_transaccion=2).extra({'fecha': get_mes})
    dinicio= query.values('fecha').annotate(monto=Sum('monto')).order_by('fecha')

    #print(dlist)
    data = \
        DataPool(
           series=
            [{'options': {
               'source': dinicio},
              'terms': ['fecha','monto']}
             ])

    def monthname(month_num):
        names ={'2016-01-01': 'Enero', '2016-02-01': 'Febrero', '2016-03-01': 'Marzo', '2016-04-01': 'Abril', '2016-05-01': 'Mayo', '2016-06-01': 'Junio',
        '2016-07-01': 'Julio', '2016-08-01': 'Agosto', '2016-09-01': 'Septiembre', '2016-10-01': 'Octubre', '2016-11-01': 'Noviembre', '2016-12-01': 'Diciembre'}
        return names[month_num]

    cht = Chart(
            datasource = data,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }},
                'terms':{
                  'fecha': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'MONTO TOTAL GASTOS POR MES'},
               'xAxis': {
                    'title': {
                       'text': 'MES'}}},
            x_sortf_mapf_mts = (None, monthname, False))

    #Grafico 2
    data2 = \
        DataPool(
           series=
            [{'options': {
               'source': Transaccion.objects.values('nombre_entrada','nombre_entrada__name').filter(tipo_transaccion=2).annotate(monto=Sum('monto'))},
              'terms': ['nombre_entrada__name','monto']}
             ])

    cht2 = Chart(
            datasource = data2,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }},
                'terms':{
                  'nombre_entrada__name': [
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
               'source': Transaccion.objects.values('consumidor__name').annotate(monto=Sum('monto')).filter(nombre_entrada=10)}, #fecha__month=date.today().month)},
              'terms': ['consumidor__name','monto']}
             ])

    cht3 = Chart(
            datasource = data3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'stacking': False},
                'terms':{
                  'consumidor__name': [
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
               'source': Transaccion.objects.values('consumidor__name').annotate(monto=Sum('monto')).filter(nombre_entrada=3)}, #,fecha__month=date.today().month)},
              'terms': ['consumidor__name','monto']}
             ])

    cht4 = Chart(
            datasource = data4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'stacking': False},
                'terms':{
                  'consumidor__name': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Gasto en combustible por Persona'},
               'xAxis': {
                    'title': {
                       'text': 'Consumidor'}}})

    #Grafico 5 ingresos mensuales 2016
    get_mes = connection.ops.date_trunc_sql('month', 'fecha')
    query= Transaccion.objects.filter(fecha__year=2016,tipo_transaccion=1).extra({'fecha': get_mes})
    dinicio= query.values('fecha').annotate(monto=Sum('monto')).order_by('fecha')

    #print(dlist)
    data5 = \
        DataPool(
           series=
            [{'options': {
               'source': dinicio},
              'terms': ['fecha','monto']}
             ])


    cht5 = Chart(
            datasource = data5,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False,
                    'dataLabels': {
                    'enabled': True
                  }},
                'terms':{
                  'fecha': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'INGRESOS MENSUALES AÑO 2016'},
               'xAxis': {
                    'title': {
                       'text': 'MES'}}},
            x_sortf_mapf_mts = (None, monthname, False))

    #Grafico 6 tipos de gasto por persona Alexis
    data6 = \
        DataPool(
           series=
            [{'options': {
               'source': Transaccion.objects.values('nombre_entrada','nombre_entrada__name').filter(tipo_transaccion=2,consumidor__id=1).annotate(monto=Sum('monto'))},
              'terms': ['nombre_entrada__name','monto']}
             ])

    cht6 = Chart(
            datasource = data6,
            series_options =
              [{'options':{
                  'type': 'bar',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }
                },
                'terms':{
                  'nombre_entrada__name': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Total Gastos ALEXIS'},
               'xAxis': {
                    'title': {
                       'text': 'Entradas'}}})

    #Grafico 7 tipos de gasto por persona francisco
    data7 = \
        DataPool(
           series=
            [{'options': {
               'source': Transaccion.objects.values('nombre_entrada','nombre_entrada__name').filter(tipo_transaccion=2,consumidor__id=4).annotate(monto=Sum('monto'))},
              'terms': ['nombre_entrada__name','monto']}
             ])

    cht7 = Chart(
            datasource = data7,
            series_options =
              [{'options':{
                  'type': 'bar',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }
                },
                'terms':{
                  'nombre_entrada__name': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Total Gastos Francisco'},
               'xAxis': {
                    'title': {
                       'text': 'Entradas'}}})

    #Grafico 7 tipos de gasto por persona Camilo
    data8 = \
        DataPool(
           series=
            [{'options': {
               'source': Transaccion.objects.values('nombre_entrada','nombre_entrada__name').filter(tipo_transaccion=2,consumidor__id=3).annotate(monto=Sum('monto'))},
              'terms': ['nombre_entrada__name','monto']}
             ])

    cht8 = Chart(
            datasource = data8,
            series_options =
              [{'options':{
                  'type': 'bar',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }
                },
                'terms':{
                  'nombre_entrada__name': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Total Gastos Camilo'},
               'xAxis': {
                    'title': {
                       'text': 'Entradas'}}})

    #Grafico 8 tipos de gasto por persona Juan
    data9 = \
        DataPool(
           series=
            [{'options': {
               'source': Transaccion.objects.values('nombre_entrada','nombre_entrada__name').filter(tipo_transaccion=2,consumidor__id=2).annotate(monto=Sum('monto'))},
              'terms': ['nombre_entrada__name','monto']}
             ])

    cht9 = Chart(
            datasource = data9,
            series_options =
              [{'options':{
                  'type': 'bar',
                  'stacking': False,
                  'dataLabels': {
                    'enabled': True
                  }
                },
                'terms':{
                  'nombre_entrada__name': [
                    'monto']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Total Gastos Juan'},
               'xAxis': {
                    'title': {
                       'text': 'Entradas'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('production/chartjs.html',{'weatherchart': [cht,cht2,cht3,cht4,cht5,cht6,cht7,cht8,cht9],'data_graph': grafico},context_instance=RequestContext(request))

@login_required
def transaccion_crear(request):
    mensaje = None
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Transacción Ingresada Correctamente"
        else:
            mensaje = "Transaccion No Ingresada. Datos Incorrectos"
    else:
        form = TransaccionForm()
    return render_to_response('production/transaccion_crear.html',{'accion': 'Agregar', 'mensaje': mensaje,'form': form},context_instance=RequestContext(request))

@login_required
def transaccion_editar(request, item_id):
    mensaje = None
    obj = get_object_or_404(Transaccion, id=item_id)
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            mensaje = "Transacción Editada Correctamente"
        else:
            mensaje = "Transaccion No Editada. Datos Incorrectos"
    else:
        form = TransaccionForm(instance=obj)
    return render_to_response('production/transaccion_crear.html',{'accion': 'Editar', 'mensaje': mensaje,'form': form},context_instance=RequestContext(request))


@login_required
def transaccion_eliminar(request,item_id):
    note = get_object_or_404(Transaccion, pk=item_id).delete()
    return HttpResponseRedirect(reverse('contabilidad.views.transacciones'))
    #return render_to_response('production/transacciones.html',{'note': note},context_instance=RequestContext(request))
    #return render_to_response('production/tables_dynamic2.html',{'mensaje': "Eliminado correctamente"},context_instance=RequestContext(request))

