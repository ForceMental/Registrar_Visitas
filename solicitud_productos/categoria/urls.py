from django.urls import path
from . import views

urlpatterns = [
    # URLs para Categoria
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),  
]
