from django.shortcuts import render
from rest_framework import generics
from .models import Solicitud
from .serializers import SolicitudSerializer

class SolicitudListView(generics.ListCreateAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class SolicitudDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

