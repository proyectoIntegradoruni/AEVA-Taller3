import './page.css'
import React, { useState } from 'react';

function Registro() {
    const [nombre, setNombre] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
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
            <h1 className='Titulo'>Sign up</h1>

            <div className="inputs-container">
                <input
                    className={nombre !== "" ? "has-val input" : "input"}
                    type="text"
                    value={nombre}
                    style={{ color: nombre !== "" ? "black" : "black" }}
                    onChange={(e) => setNombre(e.target.value)}
                    placeholder="Nombre"
                    required
                />

                <input
                    className={email !== "" ? "has-val input" : "input"}
                    type="email"
                    value={email}
                    style={{ color: email !== "" ? "black" : "black" }}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                    required
                />

                <input
                    className={password !== "" ? "has-val input" : "input"}
                    type="password"
                    value={password}
                    style={{ color: password !== "" ? "black" : "black" }}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
            </div>

            <button className='Regis'>Registrar</button>
             <h3 className='Conten'>¿Ya tienes cuenta?</h3> 
        </div>
      </div>
    );
  }
  
  export default Registro;