'''from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera vista en Django.")

# Create your views here.'''

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

import cv2
import face_recognition
from deepface import DeepFace



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

        # Decodificar la imagen base64 y guardarla como archivo
        with open('imagen.jpg', 'wb') as file:
            file.write(foto.decode('base64'))

        original_image = cv2.imread('./imagen.jpg')

        # Convertir la imagen a RGB para face_recognition
        rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

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
            face_image = original_image[top:bottom, left:right]
            
            # Guardar la imagen del rostro recortado
            cv2.imwrite('rostro_recortado.jpg', face_image)

            # Utilizar DeepFace para reconocer emociones en el rostro
            result = DeepFace.analyze(face_image, actions=['emotion'])
            
            # Imprimir el resultado de la emoción
            emotions = result[0]['emotion']
            print("Emotions:", result)
            gano = max(emotions, key=emotions.get)
            '''# Dibujar un rectángulo alrededor del rostro
            cv2.rectangle(original_image, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Mostrar la emoción detectada
            cv2.putText(original_image, max(emotions, key=emotions.get), (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Mostrar la imagen con los rostros y las emociones detectadas
            cv2.imshow("Face Detection with Emotion Recognition", original_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows() '''  
            return JsonResponse({'mensaje': gano})
        else:
            print("No se detectaron rostros en la imagen.")
            return JsonResponse({'error': 'No se detectaron rostros en la imagen '}, status=400)
        print(nombre, edad, datos_recibidos)
        # Realiza alguna operación con los datos
        mensaje = f"Hola, {nombre}. Tienes {edad} años."


        # Devuelve una respuesta HTTP en formato JSON
        
    else:
        return JsonResponse({'error': 'Esta vista solo acepta solicitudes POST. '}, status=405)
