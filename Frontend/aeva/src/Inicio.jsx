import './page.css'
import Cards from "./component/Tarjetas";

function Inicio() {
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
        
        <div className='Contenido'> <div className="App">
    </div>
            <h1 className='Titulo'>AEVA</h1> 
            <h3 className='Descripcion'>Analizador de Emociones Visuales </h3> 
            <h3 className='Conten'>Con AEVA podras reconocer las emociones<br></br>
             o expresiones faciales de los demás en <br></br>
             tiempo real. </h3> 
             <button className='MoreInf'>Mas informacion</button>
        </div>
      </div>
    );
  }
  
  export default Inicio;