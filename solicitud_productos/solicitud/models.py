from django.db import models

class Solicitud(models.Model):
    ESTADO_SOLICITUD_CHOICES = (
        ('A', 'Aprobado'),
        ('P', 'Pendiente'),
        ('R', 'Rechazado'),
    )
    
    PRODUCTO_SOLICITADO_CHOICES = (
        ('alarma', 'Alarma'),
        ('boton', 'Botón'),
        ('camaras', 'Cámaras'),
    )

    id_solicitud = models.AutoField(primary_key=True)
    estado_solicitud = models.CharField(max_length=1, choices=ESTADO_SOLICITUD_CHOICES, default='P')
    empleado = models.ForeignKey('empleado.Empleado', on_delete=models.CASCADE, db_column='empleado_id_empleado')

    cantidad_solicitada = models.IntegerField()
    producto_solicitado = models.CharField(max_length=10, choices=PRODUCTO_SOLICITADO_CHOICES)

    def __str__(self):
        return f"Solicitud {self.id_solicitud} - {self.get_producto_solicitado_display()} - {self.get_estado_solicitud_display()}"
    
    
    def save(self, *args, **kwargs):
        if self.pk is None:  # Solo si es una nueva solicitud
            empleado = self.empleado
            empleado.solicitar_producto(self.producto_solicitado, self.cantidad_solicitada)
        super().save(*args, **kwargs)