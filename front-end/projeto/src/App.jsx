import { useState, createContext } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Login'
import Painel from './pages/Painel'
import Alunos from './pages/Alunos'

export const UserContext = createContext()
export const InfoContext = createContext()

export default function App() {
  const [user,setUser] = useState({'cpf':'999.999.999-99','nome':'nometeste','email':'c_emailteste','senha':'c_senhateste','unidade_id':'1','usuario':'coordenadores'})
  const [info,setInfo] = useState({'unidades':[],'alunos':[]})

  return(
    <UserContext.Provider value={[user,setUser]}>
      <InfoContext.Provider value={[info,setInfo]}>
        <BrowserRouter>
          <Routes>
              <Route path='/' element={
                <Home/>
              }/>
              <Route path='/painel' element={<Painel/>}/>
              <Route exact path='/painel/alunos' element={<Alunos/>}/>
          </Routes>
        </BrowserRouter>
      </InfoContext.Provider>
    </UserContext.Provider>
  )
}

