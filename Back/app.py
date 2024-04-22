import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://rivaslina:qEqHkwUUMrtaG61u@taller1.7ujjqcr.mongodb.net/TallerI?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/login', methods=['POST'])
def login():
    # Obtener datos de inicio de sesión del cuerpo de la solicitud
    data = request.json
    usuario = data.get('usuario')
    password = data.get('password')

    # Verificar si se proporcionaron tanto el usuario como la contraseña
    if not usuario or not password:
        return jsonify({'error': 'Usuario y contraseña son requeridos'}), 400

    # Buscar el usuario en la base de datos
    user = mongo.db.usuarios.find_one({'usuario': usuario})

    # Verificar si el usuario existe
    if user:
        # Verificar si la contraseña coincide
        if password == user['password']:
            return jsonify({'message': 'Inicio de sesión exitoso'}), 200
        else:
            return jsonify({'error': 'Credenciales inválidas'}), 401
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

def get_all_collections():
    collections = mongo.db.list_collection_names()
    if collections:
        return jsonify(collections), 200
    else:
        return jsonify({'error': 'No se encontraron colecciones'}), 404
    
@app.route('/collections', methods=['GET'])
def get_collections():
    return get_all_collections()


@app.route('/login/rostro', methods=['POST'])
def login():
    # Obtener datos de inicio de sesión del cuerpo de la solicitud
    data = request.json
    usuario = data.get('usuario')
    imagen_usuario = data.get('imagen')  # Imagen del rostro del usuario

    # Verificar si se proporcionaron tanto el usuario como la imagen
    if not usuario or not imagen_usuario:
        return jsonify({'error': 'Usuario y la imagen del rostro son requeridos'}), 400

    # Buscar el usuario en la base de datos
    user = mongo.db.usuarios.find_one({'usuario': usuario})

    # Verificar si el usuario existe
    if user:
        # Obtener la imagen del rostro del usuario de la base de datos
        imagen_usuario_bd = user['rostro']

        # Convertir las imágenes a matrices NumPy
        img_usuario_np = face_recognition.load_image_file(imagen_usuario)
        img_usuario_bd_np = face_recognition.load_image_file(imagen_usuario_bd)

        # Extraer los vectores de características (embeddings) de las imágenes
        embedding_usuario = face_recognition.face_encodings(img_usuario_np)[0]
        embedding_usuario_bd = face_recognition.face_encodings(img_usuario_bd_np)[0]

        # Comparar los vectores de características (embeddings) de las imágenes
        if face_recognition.compare_faces([embedding_usuario_bd], embedding_usuario)[0]:
            return jsonify({'message': 'Inicio de sesión exitoso'}), 200
        else:
            return jsonify({'error': 'Credenciales inválidas'}), 401
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
if __name__ == '__main__':
    app.run(debug=True)
