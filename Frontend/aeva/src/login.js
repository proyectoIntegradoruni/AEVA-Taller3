//import React, { useState } from 'react';
import './page.css'

function Login() {
    //const [email, setEmail] = useState("");
    //const [password, setPassword] = useState("");
    return (
      <div className="Inicio">
        <header className="Inicio-arriba">
            <div className="superior-izquierdo">
                <p>AEVA</p>
            </div>
            
            <div className="Superior-derecho">
                <p>Home</p>
                <p>Sign in</p>
                <p>Sign up</p>
                <p>Otro</p>
            </div>
        </header>
        <div className='Contenedor'>
            <h1 className='Titulo'>Sign in</h1> 
            
            <h3 className='Descripcion'>user </h3> 
            
            <h3 className='Descripcion'>password </h3> 
            
            <button className='MoreInf'>Iniciar Sesion</button>
             <h3 className='Conten'>¿No tienes cuenta?</h3> 
        </div>
      </div>
    );
  }
  
  export default Login;