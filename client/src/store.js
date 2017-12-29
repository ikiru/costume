import { compose, createStore, applyMiddleware } from 'redux';
import { createLogger } from 'redux-logger';
import { persistStore, autoRehydrate } from 'redux-persist';
import rootReducer from './reducers';
// import thunk from 'redux-thunk';

const store = createStore(
  rootReducer,
  compose(
    applyMiddleware(
      createLogger(),
      // thunk
    ),
    // autoRehydrate()
  )
);
persistStore(store);
export default store;