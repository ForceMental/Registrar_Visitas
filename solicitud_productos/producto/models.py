from django.db import models
from categoria.models import Categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    stock_producto = models.PositiveIntegerField()
    nombre_producto = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'producto'
