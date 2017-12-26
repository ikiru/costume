import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import Login from '../components/login/Login'
import Menu from '../components/Menu/Menu';
import Header from '../components/Header/Header';
import Footer from '../components/Footer/Footer';
import Addowners from '../components/Forms/Addowners/Addowners';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Addowners />
      </div>
      
    );
  }
}

export default App;
