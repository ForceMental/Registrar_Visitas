from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import transaction

class Empleado(AbstractUser):
    ROLES = (
        ('E', 'Ejecutivo'),
        ('J', 'Jefe'),
    )

    nombre_empleado = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    stock_disponible = models.PositiveIntegerField(default=0)
    tipo_empleado = models.CharField(max_length=1, choices=ROLES, default='E')
    empleado_jefe = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="subordinados", db_column='empleado_id_empleado')
    groups = models.ManyToManyField(Group, blank=True, related_name="empleado_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="empleado_set")


    @property
    def is_jefe(self):
        return self.tipo_empleado == 'J'

    def __str__(self):
        return self.username
    
    def clean(self):
        if self.stock_disponible < 0:
            raise ValidationError("El stock no puede ser negativo.")
        
    def incrementar_stock(self, cantidad):
        with transaction.atomic():
            self.stock_disponible += cantidad
            self.save()

    def decrementar_stock(self, cantidad):
        with transaction.atomic():
            if self.stock_disponible - cantidad < 0:
                raise ValidationError("No hay suficiente stock.")
            self.stock_disponible -= cantidad
            self.save()

