import React, { Component } from 'react';
import './Menu.css';

const Menu = (props) => {
    return (
        <div className='Menu'>
            <div className='Menu-list'>
                <ul> 
                    <li><a>HOME</a></li>
                    <li><a>NEWS</a></li>
                    <li><a>ABOUT</a></li>
                    <li><a>CONTACT</a></li>
                    <li><a>FAQ</a></li>
                    <li><a>LOGIN</a></li>
                </ul>
            </div>
        </div>
    )
}

export default Menu;