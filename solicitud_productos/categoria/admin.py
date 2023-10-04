from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria_id', 'nombre_categoria']
    search_fields = ['nombre_categoria']

admin.site.register(Categoria, CategoriaAdmin)
