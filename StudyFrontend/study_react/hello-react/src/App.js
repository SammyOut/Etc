import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    const name = 'World';
    return (
      <div>
        <p>hello {name}</p>
        {
          1 + 1 === 2?
          (<div>1 + 1 == 2</div>) : (<div> 1 + 1 != 3</div>)
        }
      </div>
    );
  }
}

export default App;
