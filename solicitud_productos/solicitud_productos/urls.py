"""solicitud_productos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from empleado.views import EmpleadoListView, EmpleadoDetailView, crear_ejecutivo_view, eliminar_productos_ejecutivo_view
from categoria.views import CategoriaListView, CategoriaDetailView
from producto.views import ProductoListView, ProductoDetailView
from solicitud.views import SolicitudListView, SolicitudDetailView
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs para Empleado
    path('empleados/', EmpleadoListView.as_view(), name='empleados-list'),
    path('empleados/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleados/crear-ejecutivo/', crear_ejecutivo_view, name='crear-ejecutivo'),
    path('empleados/<int:ejecutivo_id>/eliminar_productos/', eliminar_productos_ejecutivo_view, name='eliminar-productos-ejecutivo'),

    # URLs para Categoria
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),

    # URLs para Producto
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),

    # URLs para Solicitud
    path('solicitudes/', SolicitudListView.as_view(), name='solicitud-list'),
    path('solicitudes/<int:pk>/', SolicitudDetailView.as_view(), name='solicitud-detail'),
    
    #url para los token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]
