// form.js - form route module
const express = require('express');
const router = express.Router();
const path = require('path')

// Forms homepage
router.get('/', (req, res) => res.send('Forms homepage'));
router.get('/about', (req, res) => res.sendFile(path.resolve('public/about.html')));
router.get('/01', (req, res) => res.render('../forms/form01', {
	user: {
		firstName: 'nameFromDB',
		lastName: '',
		nickName:'nickNameFromDB'
	}
}));
// If someone (form01.pug) posts to this url, do this:
router.post('/01/results', function(req, res){
	res.setHeader('Content-Type', 'application/json');
	res.send(JSON.stringify(req.body, null, 2));
});


module.exports = router;