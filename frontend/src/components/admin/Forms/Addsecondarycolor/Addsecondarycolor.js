import React, { Component } from 'react';

import Input from '../../../ui/input/input';

class AddSecondaryColors extends Component {
    
    state = {
        addSecondaryColors:{
            color:{
                elementType:'select',
                elementConfig:{
                    options:[
                        {value:'1', displayValue:'Blue'},
                        {value:'2', displayValue:'Green'},
                        {value:'3', displayValue:'Purple'}
                    ]
                },
                value:''
            },
        }

        // loading:false
    }

    inputChangedHandler = (event, inputIdentifier) => {
        const updatedAddSecondaryColors = {
            ...this.state.addSecondaryColors
        };
        const updatedFormElement = { 
            ...updatedAddSecondaryColors[inputIdentifier]
        };
        updatedFormElement.value = event.target.value;
        updatedAddSecondaryColors[inputIdentifier] = updatedFormElement;
        this.setState({orderForm: updatedAddSecondaryColors});
    }

    render (){
        const formElementsArray = [];
        for(let key in this.state.addSecondaryColors){
            formElementsArray.push({
                id: key,
                config: this.state.addSecondaryColors[key]
            });
        }
        let form = (
            <form>              
                {formElementsArray.map(formElement => (
                    <Input 
                    key={formElement.id}
                    elementType={formElement.config.elementType} 
                    elementConfig={formElement.config.elementConfig}
                    value={formElement.config.value}
                    changed={(event) => this.inputChangedHandler(event, formElement.id)} 
                    />
                ))}
                
            </form>
        );
    

        return (
            <div>
                <h4>Enter Secondary Color</h4>
                {form}
            </div>
        );
    }
}
export default AddSecondaryColors;