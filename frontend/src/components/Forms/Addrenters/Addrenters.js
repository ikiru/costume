import React, { Component } from 'react';

import classes from './Addrenters.css';
import Input from '../../ui/Input/Input';

class AddRenters extends Component {
    
    state = {
        addRenters:{
            name:{
                elementType:'input',
                elementConfig:{
                    type:'text',
                    placeholder: 'Business Name'
                },
                value:''

            },
            address:{
                elementType:'input',
                elementConfig:{
                    type:'text',
                    placeholder: 'Business Address'
                },
                value:''

            },

            city:{
                elementType:'input',
                elementConfig:{
                    type:'text',
                    placeholder: 'City'
                },
                value:''

            },

            state:{
                elementType:'select',
                elementConfig:{
                    option:[
                        {value:'AL', displayvalue:'AL'},
                        {value:'KS', displayvalue:'KS'},
                        {value:'TX', displayvalue:'TX'}
                    ]
                },
                value:''

            },

            zipcode:{
                elementType:'input',
                elementConfig:{
                    type:'text',
                    placeholder: 'Zip Code'
                },
                value:''

            },

            phone_number:{
                elementType:'input',
                elementConfig:{
                    type:'text',
                    placeholder: 'Daytime Phone Number'
                },
                value:''

            },

            email:{
                elementType:'email',
                elementConfig:{
                    type:'email',
                    placeholder: 'Email'
                },
                value:''

            },

        }

        // loading:false
    }

    inputChangedHandler = (event, inputIdentifier) => {
        const updatedAddRenters = {
            ...this.state.addOwner
        };
        const updatedFormElement = { 
            ...updatedAddRenters[inputIdentifier]
        };
        updatedFormElement.value = event.target.value;
        updatedAddRenters[inputIdentifier] = updatedFormElement;
        this.setState({addRenters: updatedAddRenters});
    }

    render (){
        const formElementsArray = [];
        for(let key in this.state.addRenters){
            formElementsArray.push({
                id: key,
                config: this.state.addRenters[key]
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
            <div className={classes.addRenters}>
                <h4>Enter Renters Data</h4>
                {form}
            </div>
        );
    }
}
export default AddRenters;