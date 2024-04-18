import face_recognition
import cv2
from tensorflow.keras.models import load_model
import numpy as np

# Cargar el modelo pre-entrenado para reconocimiento de emociones
model = load_model('emotion_model.h5')

# Crear un diccionario de etiquetas de emociones
emotion_labels = {
    0: 'Angry',
    1: 'Disgust',
    2: 'Fear',
    3: 'Happy',
    4: 'Sad',
    5: 'Surprise',
    6: 'Neutral'
}

# Función para preprocesar la imagen para el modelo de emociones
def preprocess_input(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (48, 48))
    image = image / 255.0
    image = np.reshape(image, (1, 48, 48, 1))
    return image

# Cargar la imagen y convertirla a RGB (face_recognition trabaja con imágenes en formato RGB)
image = cv2.imread("test_image.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detectar rostros en la imagen usando face_recognition
face_locations = face_recognition.face_locations(rgb_image)

# Para cada rostro detectado
for face_location in face_locations:
    top, right, bottom, left = face_location
    
    # Extraer el rostro
    face_image = image[top:bottom, left:right]
    
    # Preprocesar el rostro para el modelo de emociones
    face_image = preprocess_input(face_image)
    
    # Predecir la emoción en el rostro
    prediction = model.predict(face_image)
    label = emotion_labels[np.argmax(prediction)]
    
    # Dibujar un rectángulo alrededor del rostro y mostrar la emoción detectada
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image, label, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Mostrar la imagen con los rostros y las emociones detectadas
cv2.imshow("Emotion Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
