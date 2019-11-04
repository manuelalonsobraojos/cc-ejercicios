# Ejercicios Tema 3

### Ejercicio 1:
**Darse de alta en algún servicio PaaS tal como Heroku, Nodejitsu, BlueMix u OpenShift.**

Para darse de alta en **Heroku** deberemos de irnos a su página oficial [Heroku](https://www.heroku.com).  
Una vez en la página accederemos al formulario de registro y lo rellenaremos con nuestros datos.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura2.png)

Una vez rellenado el formulario haremos clic en el botón de crear cuenta y nos pedirá que accedamos al correo electrónico para confirmar el registro.
Una vez hemos accedido al correo, accederemos al enlace de confirmación y nos pedirá que ingresemos una contraseña. Una vez aceptada la contrasela nos dará la bienvenida al servicio Heroku.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura1.png)

Una vez acabado el proceso de registro ya podremos utilizar el servicio Heroku.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura3.png)


### Ejercicio 2:
**Crear una aplicación en OpenShift o en algún otro PaaS en el que se haya dado uno de alta. Realizar un despliegue de prueba usando alguno de los ejemplos.**
Accederemos a [OpenShift](https://www.openshift.com) y nos daremos de alta logueandonos con nuestra cuenta de github. Deberemos autorizar que OpenShift acceda a los datos de nuestra cuenta de github.
Una vez hemos accedido crearemos una nueva aplicación, en nuestro caso crearemos una app en python con Django seleccionandolo del catálogo que nos ofrece.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura4.png)

Una vez seleccionado deberemos de introducir el nombre de la app y un repositorio de github.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura5.png)

Una vez introducido nuestra app se construira y se desplegará automáticamente

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura6.png)

En la siguiente imagen podemos ver como la app está funcionando.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura7.png)


### Ejercicio 3:
**Realizar una app en express (o el lenguaje y marco elegido) que incluya variables como en el caso anterior.**

Para este ejercicio he creado una aplicación con el framework **Flask**, la aplicación es sencilla, la aplicación muestra un mensaje de bienvenida al nombre que le pongamos en la ruta, por ejemplo si en la ruta escribimos */user/manuel* mostrará un mensaje diciendo: "bienvenido manuel"

```
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():

	
    return """
	<html>
    <head>
        <title>Home Page</title>
    </head>
    <body> 
        <h1>Pagina principal</h1>
    </body> 
</html> """ 
 

@app.route('/user/<nombre>', methods=['GET'])
def usuario(nombre):
	
    return "<h1>bienvenido %s</h1>" %(nombre)


	
	
if __name__ == "__main__":
	port=int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)
```

### Ejercicio 4:
**Crear pruebas para las diferentes rutas de la aplicación.**

Para este ejercicio creamos un archivo test.py que testeará las rutas de la aplicación del ejercicio anterior.

```
import unittest
import os
import paginaEstatica
import tempfile
from flask.ext.testing import TestCase

class paginaEstaticaTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, paginaEstatica.app.config['DATABASE'] = tempfile.mkstemp()
        paginaEstatica.app.config['TESTING'] = True
        self.app = paginaEstatica.app.test_client()
        #paginaEstatica.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(paginaEstatica.app.config['DATABASE'])


    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_name_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/user/santiago')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
```
Con este archivo hacemos dos comprobaciones, la primera comprueba que se carga la página principal, y la segunda comprueba que para un determinado nombre de usurario se cargue la página correspondiente.


### Ejercicio 5:
**Instalar y echar a andar tu primera aplicación en Heroku.**

Para desplegarlo en Heroku crearemos un proyecto y lo sincronizaremos con el repositorio de github donde se encuentre la aplicación, una vez lo tengamos sincronizado habilitaremos la opción de despliegue automático con la que cada vez que hagamos un push a nuestro repositorio de github, automáticamente se desplegará en Heroku.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura8.png)


### Ejercicio 7:
**Haz alguna modificación a tu aplicación en node.js para Heroku, sin olvidar añadir los tests para la nueva funcionalidad, y configura el despliegue automático a Heroku usando Snap CI o alguno de los otros servicios, como Codeship, mencionados en StackOverflow**

En el ejercicio anterior ya hemos visto como configurar el despliegue automático, asi que para este ejercicio lo unico que nos queda es configurar que espere a que la aplicación pase primero los test con travis.ci. Para ello debemos marcar la casilla que vemos en la siguiente imagen.

![img](https://github.com/manuelalonsobraojos/cc-ejercicios/blob/master/Ejercicios-tema3/capturas/Captura9.png)


### Ejercicio 8:
**Preparar la aplicación con la que se ha venido trabajando hasta este momento para ejecutarse en un PaaS, el que se haya elegido.**

El PaaS elegido para desplegar la aplicación básica en Flask ha sido Heroku, para realizar dicho despliegue debemos de contar con dos archivos específicos en el repositorio de github:

- El archivo Procfile que no tiene ninguna extensión y que contendrá la orden para ejecutar la aplicación. En este caso para ejecutar la aplicación básica en Flask, el archivo Procfile contendrá esta línea: ```web: python ejercicio3.py 0.0.0.0:5000```

- El archivo runtime.txt, en este archivo le especificaremos la versión de python con la que debe desplegar la aplicación, en nuestro caso python-2.7.12.

En los siguientes enlaces podemos ver e repositorio de la aplicación, y la aplicación desplegada en Heroku.
- [Repositorio de la aplicación](https://github.com/manuelalonsobraojos/AppHeroku)
- [Aplicación desplegada en Heroku](https://ejercicio3manuelalonso.herokuapp.com/)







