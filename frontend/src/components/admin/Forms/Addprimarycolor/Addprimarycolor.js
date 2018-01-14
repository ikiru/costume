import React, { Component } from 'react';

// import Input from '../../../ui/input/input';
import { FormGroup, FormControl, ControlLabel, HelpBlock } from 'react-bootstrap'

class AddPrimaryColors extends Component {
    
    // state = {

    // inputChangedHandler = (event, inputIdentifier) => {
    //     const updatedAddPrimaryColors = {
    //         ...this.state.addPrimaryColors
    //     };
    //     const updatedFormElement = { 
    //         ...updatedAddPrimaryColors[inputIdentifier]
    //     };
    //     updatedFormElement.value = event.target.value;
    //     updatedAddPrimaryColors[inputIdentifier] = updatedFormElement;
    //     this.setState({orderForm: updatedAddPrimaryColors});
    // }

    render (){
        // const formElementsArray = [];
        // for(let key in this.state.addPrimaryColors){
        //     formElementsArray.push({
        //         id: key,
        //         config: this.state.addPrimaryColors[key]
        //     });
        // )
    return (
      <div>
        <form>
          <FormGroup
          >
            <ControlLabel>Enter Primary Color</ControlLabel>
            <FormControl
            />
            <FormControl.Feedback />
            <HelpBlock>Validation is based on string length.</HelpBlock>
          </FormGroup>
        </form>
      </div>
    )
  }
}

export default AddPrimaryColors;