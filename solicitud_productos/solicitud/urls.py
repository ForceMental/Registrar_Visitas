from django.urls import path
from . import views

urlpatterns = [

    # URLs para Solicitud
    path('solicitudes/', views.SolicitudListView.as_view(), name='solicitud-list'),
    path('solicitudes/<int:pk>/', views.SolicitudDetailView.as_view(), name='solicitud-detail'),
    
    
]
