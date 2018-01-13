import React, { Component } from 'react';

import classes from './Addprimarycolor.css';
import Input from '../../ui/Input/Input';

class AddPrimaryColors extends Component {
    
    state = {
        addPrimaryColors:{
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
        const updatedAddPrimaryColors = {
            ...this.state.addPrimaryColors
        };
        const updatedFormElement = { 
            ...updatedAddPrimaryColors[inputIdentifier]
        };
        updatedFormElement.value = event.target.value;
        updatedAddPrimaryColors[inputIdentifier] = updatedFormElement;
        this.setState({orderForm: updatedAddPrimaryColors});
    }

    render (){
        const formElementsArray = [];
        for(let key in this.state.addPrimaryColors){
            formElementsArray.push({
                id: key,
                config: this.state.addPrimaryColors[key]
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
            <div className={classes.addPrimaryColors}>
                <h4>Enter Primary Color</h4>
                {form}
            </div>
        );
    }
}
export default AddPrimaryColors;