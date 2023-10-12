from django.contrib import admin
from .models import StockDisponible

@admin.register(StockDisponible)
class StockDisponibleAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad')
