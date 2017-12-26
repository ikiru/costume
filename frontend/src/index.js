import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './containers/App'
import registerServiceWorker from './registerServiceWorker';



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
