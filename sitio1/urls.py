from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from guiacontactos.views import personas
from contabilidad.views import transacciones, chart_view, transaccion_crear, index_view, transaccion_eliminar, transaccion_editar
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index_view),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^agenda/', personas),
    url(r'^transacciones/', transacciones),
    url(r'^transaccion_eliminar/(?P<item_id>[0-9]+)/$', transaccion_eliminar, name="transaccion_eliminar"),
    url(r'^transaccion_editar/(?P<item_id>[0-9]+)/$', transaccion_editar, name="transaccion_editar"),
    url(r'^chart/', chart_view),
    url(r'^login/$', 'sitio1.views.login_page',name="login"),
    url(r'^logout/$', 'sitio1.views.logout_view',name="logout"),
    url(r'^index/$', index_view),
    url(r'^prueba/$', 'sitio1.views.prueba',name="prueba"),
    url(r'^index2/$', 'sitio1.views.index2',name="index2"),
    url(r'^tables_dynamic2/$', 'sitio1.views.tables_dynamic2',name="tables_dynamic2"),
    url(r'^chartjs/$', 'sitio1.views.chartjs',name="chartjs"),
    url(r'^transaccion/crear/$', 'contabilidad.views.transaccion_crear',name="transaccion_crear"),

]
