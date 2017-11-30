import React, { Component } from 'react';
import './App.css';
import Login from '../login/Login';

import { apiClient } from '../../util/ApiClient';

class App extends Component {
    constructor(props){
        super(props);
        this.state={ 
            schema: {}
        };
    }
    getSchema(){
       var instance = apiClient();
       instance.get('/schema/')
       .then((schema) => {
           this.setState({ schema });
       })
       .catch((error) => {
           console.log(error);
       });
    }
    
    render() {
        return (
            <div className="App">

            <Login/>
            <div>
                <button onClick={(event) => this.getSchema(event)}>Click me</button>
            </div>
            </div>
            
        );
    }
}

export default App;
