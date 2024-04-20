import cv2
import face_recognition
from deepface import DeepFace

# Cargar la imagen original
image_path = './m2.jpg'
original_image = cv2.imread(image_path)

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
    
    # Dibujar un rectángulo alrededor del rostro
    cv2.rectangle(original_image, (left, top), (right, bottom), (0, 255, 0), 2)
    
    # Mostrar la emoción detectada
    cv2.putText(original_image, max(emotions, key=emotions.get), (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Mostrar la imagen con los rostros y las emociones detectadas
    cv2.imshow("Face Detection with Emotion Recognition", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
    
else:
    print("No se detectaron rostros en la imagen.")

'''from deepface import DeepFace
import cv2
import face_recognition

# Cargar la imagen
img_path = "./feliz.jpg"
image = cv2.imread(img_path)

# Convertir la imagen a RGB (necesario para face_recognition)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detectar rostros en la imagen utilizando face_recognition
face_locations = face_recognition.face_locations(rgb_image)

# Para cada rostro detectado
for (top, right, bottom, left) in face_locations:
    # Recortar el rostro de la imagen
    face_image = image[top:bottom, left:right]
    
    # Utilizar DeepFace para reconocer emociones en el rostro
    result = DeepFace.analyze(face_image, actions=['emotion'])
    
    # Imprimir el resultado de la emoción
    emotions = result[0]['emotion']
    print("Emotions:", result)
    
    # Dibujar un rectángulo alrededor del rostro
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    
    # Mostrar la emoción detectada
    cv2.putText(image, max(emotions, key=emotions.get), (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Mostrar la imagen con los rostros y las emociones detectadas
cv2.imshow("Face Detection with Emotion Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''




