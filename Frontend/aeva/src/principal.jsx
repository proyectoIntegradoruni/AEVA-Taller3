
import './page.css'
import Sidebar from './component/sidebar';

function Principal() {
    return (

        <div className="InicioP">

            <header >
                <Sidebar></Sidebar>
                <div className="Superior">
                    <h3>Home</h3>
                    <h3>Sign in</h3>
                    <h3>Sign up</h3>
                    <h3>Otro</h3>
                </div>

            </header>
            


        </div>

    );
  }

  export default Principal;