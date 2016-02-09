from django.contrib import admin
from django.db.models import Sum
from contabilidad.models import Transacciones

#admin.site.register(Transacciones)

class TransAdmin(admin.ModelAdmin):
    list_display = ('consumidor', 'monto', 'tipo_gasto', 'fecha', 'descripcion')
    list_filter = ['consumidor', 'tipo_gasto', 'fecha']
    #list_select_related = ('consumidor', 'tipo_gasto')


'''class TransaccionesAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        total = Transacciones.objects.aggregate(total=Sum('monto'))['total']
        context = {
            'total': total,
        }
        return super(TransaccionesAdmin, self).changelist_view(request, extra_context=context)

admin.site.register(Transacciones, TransaccionesAdmin)'''

admin.site.register(Transacciones, TransAdmin)


