import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'

function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <nav style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <Link to="/">Dashboard</Link>
        <Link to="/login">Login</Link>
        <Link to="/inventory">Inventory</Link>
        <Link to="/sales">Sales</Link>
        <Link to="/repairs">Repairs</Link>
      </nav>
      <Routes>
        <Route path="/" element={<h2>Dashboard Overview</h2>} />
        <Route path="/login" element={<h2>Login Authentication</h2>} />
        <Route path="/inventory" element={<h2>Inventory Management</h2>} />
        <Route path="/sales" element={<h2>Point of Sale (POS)</h2>} />
        <Route path="/repairs" element={<h2>Device Repair Tracking</h2>} />
      </Routes>
    </div>
  )
}

export default App
