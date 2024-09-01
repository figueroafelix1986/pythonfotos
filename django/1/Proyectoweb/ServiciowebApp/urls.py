from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Ruta para la vista principal de servicios
    path('', views.servicio, name="Servicios"),
    # path('details/', views.service_details,  name='service_details'),  # Otra ruta de ejemplo

]
