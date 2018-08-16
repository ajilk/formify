import { combineReducers, createStore } from 'redux';
import { Provider } from 'react-redux';

import ReactDOM from 'react-dom'
import React from 'react'
import App from './App.js';

import { Actions, jsonformsReducer } from '@jsonforms/core';
import { materialFields, materialRenderers } from '@jsonforms/material-renderers';



import schema from './schema.json'
import uischema from './uischema.json'

const store = createStore(
	combineReducers({ jsonforms: jsonformsReducer() }),  
	{
		jsonforms: {
			renderers: materialRenderers,
			fields: materialFields,
		}
	}
);

/* Can also be initialized with data */
// const data = {
//   name: 'John Doe',
//   age: 19
// };
// store.dispatch(Actions.init(data, schema, uischema));
store.dispatch(Actions.init({}, schema, uischema));


/*
	Provides the store to the children
*/
ReactDOM.render(<Provider store={store}><App /></Provider>, document.getElementById('root'));
// registerServiceWorker();