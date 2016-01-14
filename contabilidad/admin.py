from django.contrib import admin

from contabilidad.models import Transacciones


#admin.site.register(Transacciones)

class TransAdmin(admin.ModelAdmin):
    list_display = ('consumidor', 'monto', 'tipo_gasto', 'fecha', 'descripcion')
    list_filter = ['consumidor', 'tipo_gasto', 'fecha']
    #list_select_related = ('consumidor', 'tipo_gasto')

admin.site.register(Transacciones, TransAdmin)

