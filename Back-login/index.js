const express = require('express');
const  conectarDB = require('./conexion');
const bodyParser = require('body-parser');
const Usuario = require("./Modelo/usuario");
const app = express();
const cors = require("cors");
const UsuarioT = require('./Modelo/usuario');
const multer = require('multer'); // Importa multer

conectarDB();
const fs = require('fs');
app.use(bodyParser.json());


const corsOptions = {
    origin: ['https://tarea-2-six.vercel.app/','http://localhost:3000'],
    methods: ["GET","POST", "PATCH", "DELETE"]
  };

app.use(cors(corsOptions))
const PORT = process.env.PORT || 3001;


const autenticar = async (req, res) => {
  const { email, password } = req.body;

  try {
    const usuario = await UsuarioT.findOne({ email });

    if (!usuario) {
      return res.status(401).json({ mensaje: 'Credenciales inválidas' });
    }

    if (usuario.password === password) {
      // Si las credenciales son correctas, puedes devolver el usuario autenticado
      const nombreUsuario = `${usuario.nombre}`;
      res.status(200).json({ nombreUsuario });
      console.log('ok')
    } else {
      return res.status(400).json({ mensaje: 'Contraseña incorrecta' });
    }
  } catch (error) {
    console.log(error);
    res.status(500).json({ mensaje: 'Error interno del servidor' });
  }
};


const registrarUsuario = async (req, res) => {
  const { email, nombre, password } = req.body;

  try {
    // Verificar si ya existe un usuario con el mismo correo electrónico
    const usuarioExistente = await UsuarioT.findOne({ email });

    if (usuarioExistente) {
      return res.status(400).json('El correo electrónico ya está en uso');
    }

    // Crear un nuevo usuario utilizando el modelo UsuarioT
    const nuevoUsuario = new UsuarioT({ email, nombre, password });
    await nuevoUsuario.save();

    res.status(201).json('Usuario registrado exitosamente');
  } catch (error) {
    console.log(error);
    res.status(500).json('Error interno del servidor');
  }
};


app.get('/', (req, res) => {
  res.send('¡Hola desde el servidor backend!');
});
app.post('/login', autenticar);
;
app.post('/registro', registrarUsuario);

app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});
