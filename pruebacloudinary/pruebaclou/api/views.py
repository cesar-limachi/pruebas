from http.client import responses
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'mensaje': 'API RESTFULL PROYECTO FINAL'})

@api_view(['GET'])
def hoteles(request):
    lista_hoteles = Hoteles.objects.all()
    serHoteles = HotelesSerializer(lista_hoteles,many=True)
    return Response(serHoteles.data)
