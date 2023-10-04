from django.contrib import admin
from .models import Solicitud

class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['id_solicitud', 'estado_solicitud', 'empleado', 'cantidad_solicitada', 'producto_solicitado']
    search_fields = ['id_solicitud', 'estado_solicitud']
    list_filter = ['estado_solicitud', 'empleado']

admin.site.register(Solicitud, SolicitudAdmin)
