from django.shortcuts import render
from api.models import Despacho, Ventas
from rest_framework import permissions, viewsets
from api.serializer import DespachoSerializer, VentasSerializer
# Create your views here.
class DespachoViewSet(viewsets.ModelViewSet):
    queryset =  Despacho.objects.all()
    serializer_class = DespachoSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer
