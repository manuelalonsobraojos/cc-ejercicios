# Ejercicios Tema 4

### Ejercicio 1:
**Realizar una aplicación básica que use express para devolver alguna estructura de datos del modelo que se viene usando en el curso.**

Se ha creado la app con el comando ```express ejercicio```. Las dependencias se instalarán ccon el comando ```npm install```. 
El siguiente código el cual podemos encontrar en el siguiente [enlace](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/app_express/ejercicio/app.js), corresponde con la aplicación:
```
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

app.put('/ejercicio3/:nombre',
	function (req, response){
	
		var mensaje = req.params.nombre + " Ha realizado el Ejercicio 1 asignatura CC ";

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
	
```	
Una vez tenemos lista nuestra aplicación, la ejecutamos con con el comando ```node app.js```.
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio1-1.PNG)

Una vez tenemos la aplicación ejecutando, accedemos al navegador y podemos realizar dos peticiones de tipo **GET**, para ellos escribiremos en la barra de navegación las siguientes direciones:
* **http://localhost:5000/ejercicio**.
* **http://localhost:5000/ejercicio/manuel**

Para cada una de las peticiones anterior la aplicación devuelve los siguientes resultados:
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio1-2.PNG)

![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio1-3.PNG)


### Ejercicio 2
**Programar un microservicio en express (o el lenguaje y marco elegido) que incluya variables como en el caso anterior.**

Para la realización de este ejercicio he creado un microservicio en el lenguaje python. Esta aplicación devuelve resultados de la jonada de la liga Española de fútbol. [Código](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/microservicio_python/bot/app.py)

```
from flask import Flask
from flask import Response
from flask import jsonify, make_response
from playhouse.shortcuts import model_to_dict
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService

app = Flask(__name__)


@app.route('/')
def recolect():
    rService.inserDataResult()
    return 'Datos recolectados'

@app.route('/insert')
def insert():
    response = rService.addResult()

    if (response == True):
        return "true"
    else:
        return "false"

@app.route('/result/<id>')
def getResult(id):

    result = rService.getResult(int(id))

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/resultlocal/<local>')
def getResultBylocal(local):

    result = rService.getResultByLocal(local)

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/resultvisit/<visit>')
def getResultByVisit(visit):

    result = rService.getResultByVisit(visit)

    if(result is None):
        return jsonify(None)
    return jsonify(model_to_dict(result))

@app.route('/resultall')
def getAllResult():

    result = rService.getAll()

    if(result is None):
        return jsonify(None)

    resultList= []
    for item in result:
       resultList.append(model_to_dict(item))

    print(resultList)
    return make_response(jsonify(resultList), 200)

if __name__ == '__main__':
    app.run(debug=True)
```	

Para la creación de ese microservicio he utilizado el microframework de python **flask**. 
Para ejecutarlo se usará el comando ```python app.py```, tal y como podemos ver en la siguiente imagen:
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio2-1.PNG)

Una vez está ejecutando el microservicio, accedemos al navegador y escribimos en la barra de navegación la dirección **http://localhost:5000/resultall**, la cual nos devolverá en formato json una lista con todos los resultados de la jornada.
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio2-2.PNG)

### Ejercicio 3
**Crear pruebas para las diferentes rutas de la aplicación.**

En el siguiente [código](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/microservicio_python/bot/test/test_app.py) podemos ver los test realizados para las distintas rutas del microservicio:

```
import unittest
import requests
from bot.model.BaseModel import db
from bot.model.Result import Result
from bot.service.ResultService import ResultService as rService

class ResultTest(unittest.TestCase):

    def test_check_result_by_id(self):
        """
        Test que comprueba la búsqueda de un resultados por su id
        :return:
        """
        result = True

        if(rService.getResult(1) is None):
            result = False

        self.assertTrue(result)

    def test_check_result_by_name(self):
        """
                Test que comprueba la búsqueda de un resultado por su nombre de equipo local o visitante
                :return:
                """
        result = False

        if (rService.getResultByLocal("Valencia") is not None):
            result = True
        elif (rService.getResultByVisit("Valencia") is not None):
            result = True

        self.assertTrue(result)

    def test_check_all_results(self):
        """
        Test que comprueba la búsqueda de todos los resultados
        :return:
        """
        result = True

        if (rService.getAll() is None):
            result = False

        self.assertTrue(result)

    def test_check_local_score_result(self):
        """
        Test que comprueba la búsqueda del marcador local de un partido
        :return:
        """
        result = True

        if (rService.getResultLocal(1) is None):
            result = False

        self.assertTrue(result)

    def test_name_team(self):
        """
        Test que comprueba que el nombre del equipo buscado es el devuelto
        :return:
        """
        result = Result()
        name = ""
        team = "Valencia"
        if (rService.getResultByLocal("Valencia") is not None):
            result = rService.getResultByLocal("Valencia")
            name = result.getTeamLocal()
        elif (rService.getResultByVisit("Valencia") is not None):
            result = rService.getResultByVisit("Valencia")
            name = result.getTeamVisit()

        self.assertEqual(name, team)

if __name__ == '__main__':
   unittest.main()
```   

Para su ejecución deberemos de ejcutar el comando ```python test_app.py```, tal y como podemos ver en la siguiente imgen:
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio3.PNG)

### Ejercicio 5
**Usar rake, invoke o la herramienta equivalente en tu lenguaje de programación para programar diferentes tareas que se puedan lanzar fácilmente desde la línea de órdenes.**

La herramienta equivalente es **Makefile** el cual podemos ver a continuación y encontrar en el siguiente [enlace](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/microservicio_python/Makefile):

```
install:
	python setup.py install

test:
	cd bot && cd test && python test_app.py

ejecutar:
	cd bot && python app.py
```

Podemos ejecutar cada una de las ordenes que se detallan en el código, con los siguientes comandos:

* **make install**
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio5.PNG)

* **make test**
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjeercicio5-2.PNG)

* **make ejecutar**
![](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema4/imagenes/CapturaEjercicio5-3.PNG)
