import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Main from './pages/main'

function App() {

  return (
    <>
      <Router>
            <Routes>
                <Route path="/" element={<Main />} />
            </Routes>
        </Router>
    </>
  )
}

export default App
