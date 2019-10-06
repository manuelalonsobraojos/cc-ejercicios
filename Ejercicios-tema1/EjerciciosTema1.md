# Ejercicios Tema 1. Arquitecturas software para la nube

### Ejercicio 1. Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?

La aplicación que tomo como ejemplo es la desarrollada en mi TFG, que consistía en una aplicación basada en el uso de mapas interactivos.El patrón usado fue el patrón MVC (Modelo-Vista-Controlador), desarrollado con el framework de php, Symfony.

Para evolucionar la aplicación a un patrón de tipo microservicios, se podría separar los servicios de cada módulo de la aplicación y desplegarlos en la nube, y comunicar la aplicación con dichos servicios mediante el uso de una API-Rest

### Ejercicio 2. En la aplicación que se ha usado como ejemplo en el ejercicio anterior, ¿podría usar diferentes lenguajes? ¿Qué almacenes de datos serían los más convenientes?

La aplicación además de usar el lenguaje PHP, usa el lenguaje Javascript en el lado del cliente, dotando de dinamismo a la aplicación. El uso de más lenguajes está limitado al tratarse del Framework Symfony, sin embargo con una arquitectura de microservicios, el lenguaje en el que estuvieran desarrollados estos, no importaría.

El almacen de datos utilizado fue MySQL. Sin embargo cabería la posiblidad de que evolucionara hacía un almacen noSQL, como MongoDB, ya que que la estructura y cantidad de datos que maneja la aplicación es diversa.