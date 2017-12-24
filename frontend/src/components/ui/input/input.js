import React from 'react';

import classes from '.Input.css';

const input = (props) => {
    let inputElement = null;

    switch (props.inputType){
        case('input'):
            inputElement = <Input className={classes.InputElement}{...props} />;
            break;
        case('textarea'):
            inputElement = <Textarea className={classes.InputElement}{...props} />;
            break;
        case('select'):
            inputElement = <Select className={classes.InputElement}{...props} />;
            break;
        default: 
            inputElement = <Input className={classes.InputElement}{...props} />;
    }

    return (
        <div className={classes.Input}>
            <label clasName = {classes.Label}>{props.label}</label>
            {inputElement}
    );  </div>
};

export default input;
