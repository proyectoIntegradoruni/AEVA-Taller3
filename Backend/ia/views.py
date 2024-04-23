'''from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera vista en Django.")

# Create your views here.'''

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

@api_view(['POST'])
def mi_vista(request):
    if request.method == 'POST':
        # Obtiene los datos enviados desde la solicitud POST
        datos_recibidos = json.loads(request.body)
        # datos_recibidos = request.POST  Para datos enviados con Content-Type: application/x-www-form-urlencoded
        # O puedes usar
        # datos_recibidos = json.loads(request.body)  # Para datos enviados en formato JSON

        nombre = datos_recibidos.get('nombre')
        edad = datos_recibidos.get('edad')
        print(nombre, edad, datos_recibidos)
        # Realiza alguna operación con los datos
        mensaje = f"Hola, {nombre}. Tienes {edad} años."

        # Devuelve una respuesta HTTP en formato JSON
        return JsonResponse({'mensaje': mensaje})
    else:
        return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST.'}, status=405)
