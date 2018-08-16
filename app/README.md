# [JSON Forms React App](https://jsonforms.io)

Execute `npm ci` to install the prerequisites. If you want to have the latest released versions use `npm install`.  
Execute `npm start` to start the application.
 
## File Structure
* `src/schema.json` contains the JSON schema (also referred to as 'data schema')
* `src/uischema.json` contains the UI schema
* `src/index.js` is the entry point of the application and sets up the redux store 
  that contains the data, the JSON and the UI schema necessary for JSON Forms.
* `src/App.js` is the main React component and makes use of the JSON Forms Component
  in order to render a form.
