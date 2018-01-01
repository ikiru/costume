import React, { Component } from 'react';

import classes from './Addprimarycolor.css';
import Input from '../../ui/Input/Input';

class AddPrimaryColor extends Component {
    
    state = {
        addPrimaryColor:{
            color:{
                elementType:'select',
                elementConfig:{
                    options:[
                        {value:'Blue', displayvalue:'Blue'},
                        {value:'Yellow', displayvalue:'Yellow'},
                        {value:'Purple', displayvalue:'Purple'}
                    ]
                },
                value:''

            },

        }

        // loading:false
    }

    inputChangedHandler = (event, inputIdentifier) => {
        const updatedPrimaryColor = {
            ...this.state.AddPrimaryColor
        };
        const updatedFormElement = { 
            ...updatedPrimaryColor[inputIdentifier]
        };
        updatedFormElement.value = event.target.value;
        updatedPrimaryColor[inputIdentifier] = updatedFormElement;
        this.setState({updatedPrimaryColor: updatedPrimaryColor});
    }

    render (){
        const formElementsArray = [];
        for(let key in this.state.addRenters){
            formElementsArray.push({
                id: key,
                config: this.state.AddPrimaryColor[key]
            });
        }
        let form = (
            <form>
                <Input elementtType="..." element Config="..." value="..." />
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
            <div className={classes.AddPrimaryColor}>
                <h4>Enter Primary Color</h4>
                {form}
            </div>
        );
    }
}
export default AddPrimaryColor;