from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from sitio1.views import hola, raiz, current_datetime, horas_adelante
from guiacontactos.views import personas
from contabilidad.views import transacciones, chart_view
admin.autodiscover()


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', transacciones),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^agenda/', personas),
    url(r'^hola/$', hola),
    url(r'^current/$', current_datetime),
    url(r'^fecha/mas/(\d{1,2})/$',horas_adelante),
    url(r'^transacciones/', transacciones),
    url(r'^chart/', chart_view),

]
