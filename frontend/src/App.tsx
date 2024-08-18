import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Main from './pages/Main'
import UserPage from './pages/UserPage'
import PersonalPage from './pages/PersonalPage'
import Header from './components/Header'

function App() {

  return (
    <div className='h-screen w-full flex flex-col justify-start text-3xl'>
      <Header />
      <Router>
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/user/:username" element={<UserPage/>} />
                <Route path="/user/@self" element={<PersonalPage/>} />
                <Route path="*" element={<h1>404 Not Found</h1>} />
            </Routes>
        </Router>
    </div>
  )
}

export default App
