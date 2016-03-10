from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from guiacontactos.views import personas
from contabilidad.views import transacciones, chart_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', transacciones),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url(r'^agenda/', personas),
    url(r'^transacciones/', transacciones),
    url(r'^chart/', chart_view),
    url(r'^login/$', 'sitio1.views.login_page',name="login"),
    url(r'^logout/$', 'sitio1.views.logout_view',name="logout"),

]
