from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Empleado
from .serializers import EmpleadoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class EmpleadoListView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

@api_view(['POST'])
def crear_ejecutivo_view(request):
    # Comprobamos si el usuario está autenticado y es un jefe
    if not request.user.is_authenticated or not request.user.is_jefe:
        return Response({'error': 'No estás autorizado para esta operación.'}, status=status.HTTP_403_FORBIDDEN)

    username = request.data.get('username')
    password = request.data.get('password')
    nombre_empleado = request.data.get('nombre_empleado')
    apellido = request.data.get('apellido')

    # Intentamos crear el ejecutivo usando el método que se debe definir en el modelo Empleado
    try:
        ejecutivo = request.user.crear_ejecutivo(username, password, nombre_empleado, apellido)
        # Si deseas enviar datos específicos del nuevo ejecutivo, puedes usar un serializer
        return Response({'message': f'Ejecutivo {ejecutivo.username} creado exitosamente.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def eliminar_productos_ejecutivo_view(request, ejecutivo_id):
    if not request.user.is_jefe:
        return Response({'error': 'No estás autorizado para esta operación.'}, status=status.HTTP_403_FORBIDDEN)

    try:
        request.user.eliminar_productos_ejecutivo(ejecutivo_id)
        return Response({'message': f'Productos del ejecutivo {ejecutivo_id} eliminados y stock devuelto.'}, status=status.HTTP_200_OK)
    except Empleado.DoesNotExist:
        return Response({'error': 'Ejecutivo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)    
