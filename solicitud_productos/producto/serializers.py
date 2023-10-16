from rest_framework import serializers

from categoria.models import Categoria
from .models import Producto
from categoria.serializers import CategoriaSerializer

class ProductoSerializer(serializers.ModelSerializer):
    #categoria = serializers.PrimaryKeyRelatedField(source='producto.categoria.nombre_categoria', queryset=Categoria.objects.all(), required=True)
    class Meta:
        model = Producto
        fields = ['id_producto', 'stock_producto', 'nombre_producto', 'categoria']
