import { UserContext } from '../App';
import '../styles/Painel.scss'
import OpcoesPainel from '../components/OpcoesPainel';
import { useNavigate } from 'react-router-dom';
import { useState,useContext, useEffect } from 'react';
import OperacionalTitle from '../components/OperacionalTitle';



function Painel(){
    const [user,setUser] = useContext(UserContext)
    const navigate = useNavigate()


    // useEffect(() => {
    //     console.log(user)
    //     if(user.status_code == 500){
    //         navigate("/")
    //     }
    //     //Runs only on the first render
    //   }, []);
    
    return(
        <div className="home">
            <nav>
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
            <section className="operacional">
                <OperacionalTitle title={'Painel de controle'}/>
            </section>
            <OpcoesPainel/>
        </div>
    );
}

export default Painel;