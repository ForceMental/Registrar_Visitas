from django.db import models

class StockDisponible(models.Model):
    PRODUCTO_CHOICES = (
        ('alarma', 'Alarma'),
        ('boton', 'Botón'),
        ('camaras', 'Cámaras'),
    )

    producto = models.CharField(max_length=10, choices=PRODUCTO_CHOICES, unique=True)
    cantidad = models.PositiveIntegerField(default=200)  # inicializado a 200 para dar stock inicial

    def __str__(self):
        return f"{self.get_producto_display()} - {self.cantidad}"
