import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import Painel from './pages/Painel'

function App() {
  return(
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/> 
        <Route path='/painel' element={<Painel/>}/> 
      </Routes>
    </BrowserRouter>
  )
}

export default App
