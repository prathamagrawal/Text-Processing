import React, { useState, useEffect } from 'react';
import UploadFile from './components/UploadFile';
import Home from './components/Home';
import './App.css'

function App() {

  // Connecting the flask server
  // const [data, setData] = useState([{}])

  // useEffect(() => {
  //   fetch("/data").then(
  //     response => response.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // })
  return (
    <div className="container">
      <Home />
      <UploadFile />
    </div>
  )
}

export default App