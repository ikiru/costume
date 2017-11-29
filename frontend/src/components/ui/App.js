import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import Login from '../login/Login'
import Menu from '../Menu/Menu';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';

class App extends Component {
  render() {
    return (
      <div className="App">
        {/* <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header> */}
        <Header />
        <Menu />
        <Login/>
        <Footer />
      </div>
      
    );
  }
}

export default App;
