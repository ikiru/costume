import axios from 'axios';
import _ from 'lodash';
import store from '../store';
import { setToken } from '../actions'
import { URL, LOGIN } from '../config/Api';

export function InvalidCredentialsException(message) {
    this.message = message;
    this.name = 'InvalidCredentialsException';
}

export function login(email, password) {
  console.log(email);
// If you have error: 
// Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:3000' is therefore not allowed access.
// To get to the localhost:8000, you have to install a plugin "Allow-Control-Allow-Origin" for Chrome
  return axios.post(
    URL + LOGIN,
    { email,
      password
    }).then(function (response) {
        console.log('success', response)
        store.dispatch(setToken(response.data.access));
    })
    .catch(function (error) {
        // raise different exception if due to invalid credentials
        if (_.get(error, 'response.status') === 400) {
        throw new InvalidCredentialsException(error);
        }
        throw error;
    });
}

export function loggedIn() {
  return store.getState().token == null;
}
