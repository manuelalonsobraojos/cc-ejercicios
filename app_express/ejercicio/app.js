var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

app.set('port', (process.env.PORT || 5000));
app.use(express.static(__dirname + '/public'));

app.get('/ejercicio/:nombre',
	function (req, response){
	
		var mensaje = req.params.nombre + " ha realizado el Ejercicio 1 asignatura CC";

		response.send(mensaje);

	});

app.get('/ejercicio',
	function(request,response){
		response.send("Este página corresponde al ejercicio 1 de la asignatura Cloud Computing");
	});



app.listen(app.get('port'), 
	function() {
		console.log("Node app is running at localhost:" + 			app.get('port'));
	});
