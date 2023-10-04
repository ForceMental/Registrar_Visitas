from rest_framework import serializers
from .models import Producto
from solicitud.serializers import SolicitudSerializer
from categoria.serializers import CategoriaSerializer

class ProductoSerializer(serializers.ModelSerializer):
    solicitud = SolicitudSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = Producto
        fields = ['id_producto', 'stock_producto', 'nombre_producto', 'solicitud', 'categoria']
