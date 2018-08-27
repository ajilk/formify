const path = require('path');
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const forms = require('./routes/forms.js');

app.set('view engine', 'pug');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));	
app.use('/forms', forms);

app.get('/', (req, res) => res.send('Go to /forms'));
// app.get('*', (req, res) => res.sendFile(path.resolve('public/404.html')));

app.listen(3000)