from django.contrib import admin
from contabilidad.models import Transacciones,Consumidor,Tipo_transaccion,Nombre_entrada,Transaccion

class TransAdmin(admin.ModelAdmin):
    list_display = ('consumidor', 'monto', 'tipo_gasto', 'fecha', 'descripcion')
    list_filter = ['consumidor', 'tipo_gasto', 'fecha']
    #list_select_related = ('consumidor', 'tipo_gasto')

class ConsumidorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name',]

class Tipo_Tran_Admin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name',]

class Tipo_Entrada_Admin(admin.ModelAdmin):
    list_display = ('tipo_transaccion','name')
    list_filter = ['tipo_transaccion','name']

class Transaccion_Admin(admin.ModelAdmin):
    list_display = ('tipo_transaccion','consumidor', 'monto', 'nombre_entrada', 'fecha', 'descripcion')
    list_filter = ['tipo_transaccion','consumidor', 'nombre_entrada', 'fecha']


admin.site.register(Transacciones, TransAdmin)
admin.site.register(Consumidor,ConsumidorAdmin)
admin.site.register(Tipo_transaccion,Tipo_Tran_Admin)
admin.site.register(Nombre_entrada,Tipo_Entrada_Admin)
admin.site.register(Transaccion,Transaccion_Admin)



