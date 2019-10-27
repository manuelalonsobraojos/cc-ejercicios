## Ejercicios Tema 2

### Ejercicio 1
**Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).**

Para la instalación de nodejs ejecutamos el siguiente comando:
```
sudo apt install nodejs
```

Una vez ejecutado el comando anterior, ejecutamos el siguiente comando para instalar npm, el administrador de paquetes de nodejs.
```
sudo apt install npm
```

### Ejercicio 2
**Crear una descripción del módulo usando package.json. En caso de que se trate de otro lenguaje, usar el método correspondiente.**

Utilizando el archivo package.json, indicamos todas las dependencias que requiere la aplicación para funcionar, y con tan solo usar el comando `npm install` se instalan todas las dependencias.
A continuación podemos ver el package.json creado:
```
{
  "author": "Manuel Alonso Braojos",
  "name": "porrones",
  "description": "Aplicacion de apuestas en una porra",
  "version": "0.0.1",
  "main": "./prueba.js",
  "scripts": {
    "test": "mocha"
  },
  "dependencies": {
    "sqlite3": "^4.0"
  },
  "devDependencies": {
    "assert": "^1.1.2",
    "docco": "~0.6",
    "mocha": "^6.2.0",
    "chai": "^0"
  },
  "optionalDependencies": {},
  "engines": {
    "node": ">= 8"
  }
}
```

### Ejercicio 3
**Descargar el repositorio de ejemplo anterior, instalar las herramientas necesarias (principalmente Scala y sbt) y ejecutar el ejemplo desde sbt. Alternativamente, buscar otros marcos para REST en Scala tales como Finatra o Scalatra y probar los ejemplos que se incluyan en el repositorio.**

En primer lugar clonamos el repositorio ejecutando el siguiente comando:
```git clone git://github.com/JJ/spray-test my-project```

Una vez clonado el repositorio pasamos  a instalar `scala`, para ello primero deberemos instalar jdk mediate el siguiente comando:
```
sudo apt-get install default-jdk
```

Una vez instalado el `jdk` pasamos a instalar scala mediante el siguiente comando:
```
sudo apt-get install scala
```

