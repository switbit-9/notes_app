import { createStore, applyMiddleware, compose } from 'redux';

import rootReducer from './reducers';
import apiMiddleware from '../middlewares/api'

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(rootReducer, composeEnhancers(applyMiddleware(apiMiddleware)));

export default store;