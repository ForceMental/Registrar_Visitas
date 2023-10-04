from django.shortcuts import render
from rest_framework import generics
from .models import Categoria
from .serializers import CategoriaSerializer

class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
