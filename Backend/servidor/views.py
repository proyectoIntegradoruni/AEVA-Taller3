from django.shortcuts import render
from django.http import JsonResponse

import json

def mi_vista(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud
        data = json.loads(request.body)
        # Procesar los datos recibidos
        nombre = data.get('nombre')
        edad = data.get('edad')
        # Realizar acciones con los datos, por ejemplo, guardarlos en la base de datos
        # Devolver una respuesta
        response_data = {'message': 'Datos recibidos correctamente', 'nombre': nombre, 'edad': edad}
        return JsonResponse(response_data)
    else:
        # Manejar otros métodos de solicitud aquí
        return JsonResponse({'error': 'Método no permitido'}, status=405)