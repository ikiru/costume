import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';
import store from './store';

import registerServiceWorker from './registerServiceWorker';
import App from './components/ui/App';


ReactDOM.render(
    <Provider store={store}>
        <Router>
            <div>
                <App />
            </div>
        </Router> 
    </Provider>,
    document.getElementById('root')
);
registerServiceWorker();
