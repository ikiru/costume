//  this is a place to create custom errors Use it as tool for testing problem code
// just wrap code in Errorboundary tag with key attributes added to this tag.
// Error Boundaries: https://reactjs.org/docs/error-boundaries.html

import React, { Component } from 'react';

class ErrorBoundary extends Component {
    state = {
        hasError: false,
        errorMessage:''
    }

    componentDidCatch = (error, info) => {
        this.setState({hassError: true, errorMessage: error});
    }

    render() {
        if (this.state.hasError){
            return <h1>{this.state.errorMessage}</h1>;
        }else{
            return this.props.children;
        }
        
    }
}

export default ErrorBoundary;