from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_jefe']
    search_fields = ['username', 'email']
    list_filter = ['tipo_empleado']

admin.site.register(Empleado, EmpleadoAdmin)
