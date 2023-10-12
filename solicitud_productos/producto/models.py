from django.db import models
from solicitud.models import Solicitud
from categoria.models import Categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    stock_producto = models.PositiveIntegerField()
    nombre_producto = models.CharField(max_length=50)
    solicitud = models.ForeignKey('solicitud.Solicitud', on_delete=models.CASCADE, related_name='productos')  # Usamos la notación 'app_name.ModelName'
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'producto'
