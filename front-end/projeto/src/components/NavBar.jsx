import '../styles/NavBarStyle.scss'
import { UserContext } from '../App';
import { useContext } from 'react';

function NavBar(){
    const [user,setUser] = useContext(UserContext)
    
    return(
        <nav className="navbar">
            <div className='nav-content'>
                <div className='nav-items'>
                    <span className='nome1'>Unidade</span>
                    <span>|</span>
                    <span className='nome2'>{user.unidade_id}</span>
                </div>
                <div className='nav-items'>
                    <span className='nome1'>{user.cpf}</span>
                    <span>|</span>
                    <span className='nome2'>{user.nome}</span>
                </div>
            </div>
        </nav>
    );
}

export default NavBar;