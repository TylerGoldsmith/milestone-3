import React, { Component } from "react";
import { Container } from './index';
import '../assets/css/style.css';

class App extends Component {
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