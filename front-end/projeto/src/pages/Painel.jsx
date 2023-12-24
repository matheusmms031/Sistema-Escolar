import { UserContext } from '../App';
import '../styles/Painel.scss'
import { useState,useContext, useEffect } from 'react';



function Painel(){
    const [user,setUser] = useContext(UserContext)
    
    return(
        <div className="painel">
            <nav>
                <div className='nav-content'>
                    <div className='nav-items'>
                        <span className='nome1'>Lagoa Santa</span>
                        <span>|</span>
                        <span className='nome2'>1</span>
                    </div>
                    <div className='nav-items'>
                        <span className='nome1'>999.999.999-99</span>
                        <span>|</span>
                        <span className='nome2'>Matheus Magalhães Monteiro Sales</span>
                    </div>
                </div>      
            </nav>
        </div>
    );
}

export default Painel;