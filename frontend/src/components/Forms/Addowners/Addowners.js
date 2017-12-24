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
                        {value:'AL', displayvalue:'AL'}
                        {value:'KS', displayvalue:'KS'}
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

        loading:false
    }

    render (){
        let form = (
            <form>
                <Input elementtType="..." element Config="..." value="..." />
            </form>
        )
    }
}