from django.contrib import admin
from .models import Servicio

# Register your models here.


class ServicioAdmin(admin.ModelAdmin):
    # esto es para que salgan las dos columnas de solo lectura
    readonly_fields = ('created', 'updated')


admin.site.register(Servicio, ServicioAdmin)
