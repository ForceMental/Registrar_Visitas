from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.db import transaction
from producto.models import Producto
from django.db.models import F


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

    def crear_ejecutivo(self, username, password, nombre_empleado, apellido, **other_fields):
        """
        Permite a un jefe crear un nuevo ejecutivo.
        """
        if not self.is_jefe:
            raise PermissionError("No tienes permisos para crear un nuevo ejecutivo.")

        if Empleado.objects.filter(username=username).exists():
            raise ValueError("Ya existe un empleado con ese nombre de usuario.")

        # Crear el nuevo ejecutivo
        ejecutivo = Empleado.objects.create_user(
            username=username,
            password=password,
            nombre_empleado=nombre_empleado,
            apellido=apellido,
            tipo_empleado='E',  # Ejecutivo
            
        )
        return ejecutivo
   
    def solicitar_producto(self, tipo_producto, cantidad):
    # Usamos un bloque de transacción para asegurarnos de que todas las operaciones son atómicas.
        with transaction.atomic():
            try:
                producto = Producto.objects.get(nombre_producto=tipo_producto)  # Cambia "tipo_producto" por "nombre_producto"
            
            # Verificamos si hay stock suficiente.
                if producto.stock_producto < cantidad:
                    raise ValueError("No hay suficiente stock en el inventario global.")

            # Actualizamos el stock del producto.
                producto.stock_producto = F('stock_producto') - cantidad
                producto.save()

            # Actualizamos el stock del empleado.
                self.stock_disponible = F('stock_disponible') + cantidad
                self.save()

            except Producto.DoesNotExist:
                raise ValueError(f"No existe un producto con el nombre {tipo_producto}.")
 
    
       

    def devolver_producto(self, producto_id, cantidad):
        producto = Producto.objects.get(pk=producto_id)
        if self.stock_disponible < cantidad:
            raise ValueError("El ejecutivo no tiene suficiente stock para devolver.")
        producto.stock_producto += cantidad
        producto.save()
        self.stock_disponible -= cantidad
        self.save()
      
    from django.db import transaction

    def eliminar_productos_ejecutivo(self, ejecutivo_id):
        if not self.is_jefe:
            raise PermissionError("Solo un jefe puede realizar esta acción.")

        from solicitud.models import Solicitud  # Importación local del modelo Solicitud

        try:
            ejecutivo = Empleado.objects.get(pk=ejecutivo_id, tipo_empleado='E')
        except Empleado.DoesNotExist:
            raise ValueError(f"No existe un ejecutivo con ID {ejecutivo_id}")

        solicitudes = Solicitud.objects.filter(empleado=ejecutivo)
        productos_a_actualizar = []

        for solicitud in solicitudes:
            producto = solicitud.producto
            producto.stock_producto += solicitud.cantidad_solicitada
            productos_a_actualizar.append(producto)

        with transaction.atomic():
            Solicitud.objects.filter(empleado=ejecutivo).delete()
            Producto.objects.bulk_update(productos_a_actualizar, ['stock_producto'])

