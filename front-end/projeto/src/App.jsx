import { useState, createContext } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import Painel from './pages/Painel'

export const UserContext = createContext()

export default function App() {
  const [user,setUser] = useState({'data':'teste'})

  return(
    <UserContext.Provider value={[user,setUser]}>
      <BrowserRouter>
        <Routes>
            <Route path='/' element={
              <Home/>
            }/>
            <Route path='/painel' element={<Painel/>}/>
        </Routes>
      </BrowserRouter>
    </UserContext.Provider>
  )
}

