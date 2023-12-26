import { useState, createContext } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Login'
import Painel from './pages/Painel'
import Alunos from './pages/Alunos'

export const UserContext = createContext()

export default function App() {
  const [user,setUser] = useState({'cpf':'999.999.999-99','nome':'nometeste','email':'emailteste','senha':'senhateste','unidade_id':'unidadeteste','usuario':'coordenadores'})

  return(
    <UserContext.Provider value={[user,setUser]}>
      <BrowserRouter>
        <Routes>
            <Route path='/' element={
              <Home/>
            }/>
            <Route path='/painel' element={<Painel/>}/>
            <Route exact path='/painel/alunos' element={<Alunos/>}/>
        </Routes>
      </BrowserRouter>
    </UserContext.Provider>
  )
}

