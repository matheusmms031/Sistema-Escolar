import { UserContext } from '../App';
import '../styles/Painel.scss'
import { useNavigate } from 'react-router-dom';
import { useState,useContext, useEffect } from 'react';
import OperacionalTitle from '../components/OperacionalTitle';
import NavBar from '../components/NavBar';
import PainelBox from '../components/PainelBox';



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
            <NavBar/>
            <OperacionalTitle title={'Painel de controle'}/>
            <PainelBox page={true}>
                <span>Teste</span>
            </PainelBox>
        </div>
    );
}

export default Painel;