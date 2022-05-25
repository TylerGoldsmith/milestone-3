import React, { Component, useState } from "react";
import { Container } from './index';
import '../assets/css/style.css';

class App extends Component {
  const [token, setToken] = useState();
  if(!token)
  render() {
    return (
      <div className="App">

        <p>
          <Container />
          App.js Test
        </p>
      </div>
    );
  }
}

export default App;