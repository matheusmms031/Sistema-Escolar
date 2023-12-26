import NavBar from '../components/NavBar';
import PainelBox from '../components/PainelBox';
import { useState,useContext, useEffect } from 'react';
import OperacionalTitle from '../components/OperacionalTitle';

function Alunos(){
    return(
        <div className="home">
            <NavBar/>
            <OperacionalTitle title={'Painel de controle'}/>
            <PainelBox page={false}>
                <span>alunos</span>
            </PainelBox>
        </div>
    )
}

export default Alunos;