import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
// import Login from '../components/login/Login'
// import Menu from '../components/Menu/Menu';
// import Header from '../components/Header/Header';
// import Footer from '../components/Footer/Footer';

// Forms
import Addowners from '../components/admin/forms/addowners/addOwners'
import Addrenters from '../components/admin/forms/addrenters/addRenters'
import Addprimarycolors from '../components/admin/forms/addprimarycolor/addPrimaryColor'
import Addsecondarycolors from '../components/admin/forms/addsecondarycolor/addSecondaryColor'


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
