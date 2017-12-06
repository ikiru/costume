import React, { Component } from 'react';
import './Updatecostumes';

const updatecostumes = (props) => {
    return(
        <div className='Updatecostume'>
        <h2> Update costumes that need descritpion checked </h2>
        
        // Image of the costume to be gotten from the app
        
        
        // Description feild which should be a textarea of the costume
        
                    <div>
                        <p> Description of the costume </p>
                            <input 
                            type='textarea'
                            placeholder='Description'/>
                    </div>
        
        // QR code for the costume
        
                    <div>
                        <p> QR code for this costume.</p>
        
                        <p> This feild cannot be edited if you need to replace QR code please update the app.</p>
                    </div>
        
        // Size of the costume dropdown menu
        
                    <div>
                        <input 
                        type='text'
                        placeholder='size'/>
                    </div>
        
        // Period of the costume
        
                    <div>
                        <input 
                        type='text'
                        placeholder='period'/>
                    </div>
        
        // Primary color of the costume
        
                    <div>
                        <p>Add the primary color of the costume</p>
                            <input 
                            type='text'
                            placeholder='Primary Color of the costume'/>
                    </div>
        
        // Secondary color of the costume
        
                    <div>
                        <p>Add the secondary color of the costume</p>
                            <input 
                            type='text'
                            placeholder='Secondary Color of the costume'/>
                    </div>
        
        //Shows the costume could be usded for 
        
                    <div>
                        <p>Add any shows that this outfit maybe used for.</p>
                            <input 
                            type='text'
                            placeholder='shows'/>
                    </div>
            )
        }
        

        </div>
    )
}


export default updatecostumes;