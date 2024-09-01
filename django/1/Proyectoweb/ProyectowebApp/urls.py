from django.urls import include, path
from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),
    # path('servicios/', views.servicio, name="Servicios"),
    #path('tienda/', views.tiendas, name="Tienda"),
    # path('blog/', views.blog, name="Blog"),
    # path('contacto/', views.contacto, name="Contacto"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
