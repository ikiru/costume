import axios from 'axios';
import store from '../store';
import { URL } from '../config/Api';

export const apiClient = function() {
        const token = store.getState().token;
        console.log(token)
        const params = {
            baseURL: URL,
            // need the authorization with token to access the api
            headers: {'Authorization': 'Bearer ' + token}
        };
        return axios.create(params);
}