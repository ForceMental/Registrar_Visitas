from django.db.models.signals import post_save
from django.dispatch import receiver
from solicitud.models import Solicitud
from stock_disponible_producto.models import StockDisponible 

@receiver(post_save, sender=Solicitud)
def actualizar_stock(sender, instance, **kwargs):
    if instance.estado_solicitud == 'A':
        stock = StockDisponible.objects.get(producto__nombre_producto=instance.producto_solicitado)
        stock.cantidad -= instance.cantidad_solicitada
        stock.save()
