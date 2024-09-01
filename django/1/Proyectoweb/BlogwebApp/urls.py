from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Ruta para la vista principal de servicios
    path('', views.blog, name="Blog"),
    path('categoria/<categoria_id>', views.categoria, name='categoria'),

]
