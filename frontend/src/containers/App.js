import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
// import Login from '../components/login/Login'
// import Menu from '../components/Menu/Menu';
// import Header from '../components/Header/Header';
// import Footer from '../components/Footer/Footer';

// Forms
import Addowners from '../components/Forms/Addowners/Addowners';
import Addrenters from '../components/Forms/Addrenters/Addrenters';
import Addprimarycolors from '../components/Forms/Addprimarycolor/Addprimarycolor';
import Addsecondarycolors from '../components/Forms/Addsecondarycolor/Addsecondarycolor';


class App extends Component {
  render() {
    return (
      
      <div className="App">
        <Addowners />
        <Addrenters />
        <Addprimarycolors />
        <Addsecondarycolors />
      </div>
      
    );
  }
}

export default App;
