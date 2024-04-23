'''from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera vista en Django.")

# Create your views here.'''

'''from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

import cv2
import face_recognition
from deepface import DeepFace
import base64'''

import face_recognition
from deepface import DeepFace
import base64
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import numpy as np
import cv2

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
        foto = datos_recibidos.get('foto')

        # Obtener los datos base64
        base64_data = foto.split(",")[1]

        # Decodificar los datos base64 en una matriz numpy
        decoded_data = base64.b64decode(base64_data)

        # Convertir los datos decodificados a una matriz numpy
        nparr = np.frombuffer(decoded_data, np.uint8)

        # Decodificar la matriz numpy en una imagen
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Convertir la imagen de BGR a RGB (face_recognition requiere imágenes en formato RGB)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Detectar rostros en la imagen usando face_recognition
        face_locations = face_recognition.face_locations(rgb_image)

        # Verificar si se detectaron rostros
        if face_locations:
            # Tomar la primera ubicación de rostro detectada
            top, right, bottom, left = face_locations[0]
            
            # Ajustar las coordenadas del recorte para incluir un poco más alrededor de la cabeza
            extra_margin = 30  # Puedes ajustar este valor según sea necesario
            top = max(0, top - extra_margin)
            right = min(rgb_image.shape[1], right + extra_margin)
            bottom = min(rgb_image.shape[0], bottom + extra_margin)
            left = max(0, left - extra_margin)
            
            # Recortar la región del rostro de la imagen original
            face_image = image[top:bottom, left:right]
            
            # Guardar la imagen del rostro recortado
            cv2.imwrite('rostro_recortado.jpg', face_image)

            # Utilizar DeepFace para reconocer emociones en el rostro
            result = DeepFace.analyze(face_image, actions=['emotion'])
            
            # Imprimir el resultado de la emoción
            emotions = result[0]['emotion']
            resultadoo = max(emotions, key=emotions.get)
            print("Emotions:", result)
            '''
            # Dibujar un rectángulo alrededor del rostro
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Mostrar la emoción detectada
            cv2.putText(image, max(emotions, key=emotions.get), (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Mostrar la imagen con los rostros y las emociones detectadas
            cv2.imshow("Face Detection with Emotion Recognition", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()   '''
            
        else:
            print("No se detectaron rostros en la imagen.")
            mensaje = "No se detectaron rostros en la imagen."
            return JsonResponse({'mensaje': mensaje})

        print(nombre, edad, datos_recibidos)
        # Realiza alguna operación con los datos
        mensaje = f"La emocion detectada es {resultadoo}"

        # Devuelve una respuesta HTTP en formato JSON
        return JsonResponse({'mensaje': mensaje})
    else:
        return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST.'}, status=405)