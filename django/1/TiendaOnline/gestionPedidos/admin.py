from django.contrib import admin

from gestionPedidos.models import *
# Register your models here.

#para que salgan las columnas 
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion")
    #busqueda
    search_fields=("nombre","direccion")
    
class ArticulosAdmin(admin.ModelAdmin):
    # Para filtrar datos
    list_filter = ("seccion",)  # Tupla con un solo elemento
    
class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"


#agregar en el panel de administracion tabla de clientes
admin.site.register(Clients,ClientesAdmin)
admin.site.register(Articulo ,ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)