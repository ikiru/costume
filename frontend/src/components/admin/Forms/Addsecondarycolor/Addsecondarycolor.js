import React, { Component } from 'react';

import { FormGroup, FormControl, ControlLabel, HelpBlock } from 'react-bootstrap'

class AddSecondaryColors extends Component {


    // inputChangedHandler = (event, inputIdentifier) => {
    //     const updatedAddSecondaryColors = {
    //         ...this.state.addSecondaryColors
    //     };
    //     const updatedFormElement = { 
    //         ...updatedAddSecondaryColors[inputIdentifier]
    //     };
    //     updatedFormElement.value = event.target.value;
    //     updatedAddSecondaryColors[inputIdentifier] = updatedFormElement;
    //     this.setState({orderForm: updatedAddSecondaryColors});
    // }

  render (){
      // const formElementsArray = [];
      // for(let key in this.state.addSecondaryColors){
      //     formElementsArray.push({
      //         id: key,
      //         config: this.state.addSecondaryColors[key]
      //     });
      // }

    //   <DropdownButton
    //   bsStyle={title.toLowerCase()}
    //   title={title}
    //   key={i}
    //   id={`dropdown-basic-${i}`}
    // >
  

    return (
      <div>
        <form>
          <FormGroup
          >
            <ControlLabel>Enter Second Color</ControlLabel>
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
export default AddSecondaryColors;