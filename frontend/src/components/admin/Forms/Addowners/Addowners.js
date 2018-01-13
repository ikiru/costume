import React, { Component } from 'react';

import classes from './Addowners.css';
import Input from '../../ui/Input/Input';

class Addowners extends Component {
    
    state = {
        addOwners:{
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
                        options:[
                            {value:'AL', displayValue:'AL'},
                            {value:'KS', displayValue:'KS'},
                            {value:'TX', displayValue:'TX'}
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
        const updatedAddOwners = {
            ...this.state.addOwners
        };
        const updatedFormElement = { 
            ...updatedAddOwners[inputIdentifier]
        };
        updatedFormElement.value = event.target.value;
        updatedAddOwners[inputIdentifier] = updatedFormElement;
        this.setState({addOwners: updatedAddOwners});
    }

    render (){
        const formElementsArray = [];
        for(let key in this.state.addOwners){
            formElementsArray.push({
                id: key,
                config: this.state.addOwners[key]
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
            <div className={classes.addOwners}>
                <h4>Enter Owners Data</h4>
                {form}
            </div>
        );
    }
}
export default Addowners;