import { connect } from 'react-redux';
import { JsonForms } from '@jsonforms/react';
import React from 'react';
import { getData } from '@jsonforms/core';

const App = ({dataAsString}) => (<div><JsonForms/><pre>{dataAsString}</pre></div>
);

// Looks important
/*
	Takes state as a paramter
	Stringifies it then connects it to other components
	mapStateToProps(state) {
		return { 
			dataAsString: JSON.stringify(getData(state), null, 2) 
		}
	}
*/
const mapStateToProps = state => {
  return { dataAsString: JSON.stringify(getData(state), ["age"], 2) }
};


export default connect(mapStateToProps, null)(App);
