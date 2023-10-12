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


    cantidad_solicitada = models.IntegerField()
    producto_solicitado = models.CharField(max_length=10, choices=PRODUCTO_SOLICITADO_CHOICES)

    def __str__(self):
        return f"Solicitud {self.id_solicitud} - {self.get_producto_solicitado_display()} - {self.get_estado_solicitud_display()}"
    
    