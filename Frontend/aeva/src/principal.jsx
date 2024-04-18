
import './page.css'
import Sidebar from './component/sidebar';
function Principal() {
    return (
      
        <div className="InicioP">
            
            <header className="Inicio-arriba">
                <Sidebar></Sidebar>
                <div className="Superior">
                    <h3>Home</h3>
                    <h3>Sign in</h3>
                    <h3>Sign up</h3>
                    <h3>Otro</h3>
                </div>
                
            </header>
            <div className="ContenidoP">
                <h2 >Bienvenido<br ></br> a AEVA</h2> 
                <h3 >Comencemos el <br ></br>reconocer emociones</h3> 
            </div>
            
   
        </div>
      
    );
  }
  
  export default Principal;