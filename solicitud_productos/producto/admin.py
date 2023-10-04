from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'stock_producto', 'categoria']
    search_fields = ['nombre_producto']
    list_filter = ['categoria']

admin.site.register(Producto, ProductoAdmin)
