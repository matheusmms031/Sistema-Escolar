import { UserContext } from '../App';
import '../styles/Painel.scss'
import { Link, useNavigate } from 'react-router-dom';
import { useState,useContext, useEffect } from 'react';
import OperacionalTitle from '../components/OperacionalTitle';
import NavBar from '../components/NavBar';
import PainelBox from '../components/PainelBox';
import Card from '../components/Card';


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
                <Link to={'/painel/alunos'} style={{'textDecoration':'none'}}><Card title={'Alunos'} about={'Sobre'}/></Link>
            </PainelBox>
        </div>
    );
}

export default Painel;