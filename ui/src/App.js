import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react'

function App() {
  const [userData, setUserData] = useState(null)

  const fetchData = () => fetch('/t', { method: 'GET' })
    .then((resp) => resp.json())
    .then(data => setUserData(data))
    .catch(err => console.log(err))

  useEffect(() => { fetchData() }, [])

  useEffect(() => console.log('u',  userData), [userData])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Here's my data:
        </p>
        {userData && <p>{userData.name}</p>}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
