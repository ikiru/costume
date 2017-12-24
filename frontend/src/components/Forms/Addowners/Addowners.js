import React from 'react';

import classes from './Addowners.css';
import Input from '../../../UI/Input/Input';

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

    render (){
        const formElementsArray = [];
        for(let key in this.state.addOwners){
            formElementsArray.push({
                id: key,
                config: this.state.addOwners[Key]
            });
        }
        let form = (
            <form>
                <Input elementtType="..." element Config="..." value="..." />
                {formElementsArray.map(formElement => (
                    <Input 
                    key={formElement.id}
                    elementType={formElement.config.elementtType} 
                    elementConfig={formElement.config.elementtConfig}
                    value={formElement.config.value} 
                    />
                ))}
                <Button btnType="Success">ORDER</Button>
            </form>
        )
    };

    return (
        <div className={classes.addOwners}>
            <h4>Enter your Owner Data</h4>
            {form}
        </div>
    );
}