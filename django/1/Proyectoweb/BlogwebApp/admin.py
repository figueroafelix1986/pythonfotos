from django.contrib import admin
from .models import *

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    # esto es para que salgan las dos columnas de solo lectura
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    # esto es para que salgan las dos columnas de solo lectura
    readonly_fields = ('created', 'updated')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
# Register your models here.
