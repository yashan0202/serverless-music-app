import logo from './logo.svg';
import './App.css';
import "./index.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hi this is a test for Dove Music. 
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Dove Music
        </a>
      </header>
    </div>
  );
}

export default App;
