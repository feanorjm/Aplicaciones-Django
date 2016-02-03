from django.contrib import admin

from guiacontactos.models import Personas


#admin.site.register(Personas)

class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'direccion', 'oficio', 'descripcion')
    list_filter = ['nombre', 'apellido', 'oficio']
    #list_select_related = ('consumidor', 'tipo_gasto')

admin.site.register(Personas, GuiaAdmin)