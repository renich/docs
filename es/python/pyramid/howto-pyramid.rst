==============
HowTo: Pyramid
==============
----------------------------------------
Instalación y Uso de Pyramid (framework)
----------------------------------------

:Autor: 
    Renich Bon Ciric <renich@woralelandia.com>

:Licencia: 
    FDL_ 1.3 o >

:Versión:
    |version|

.. raw:: pdf

    PageBreak oneColumn

.. contents::

.. section-numbering::

.. raw:: pdf

    PageBreak oneColumn


Descripción
===========
En este HowTo, vamos a estudiar como instalar y usar Pyramid_.

.. raw:: pdf

    PageBreak oneColumn

Instalación
===========

Para instalarlo, hay que seguir los siguientes pasos:

.. code-block:: Bash
    :include: instalacion.bash

.. raw:: pdf

    PageBreak oneColumn

Uso
===
Ahora, vamos a estudiar cómo usar Pyramid_ para crear aplicaciones simples; usando diferentes las diferentes herramientas provistas.

.. raw:: pdf

    PageBreak oneColumn

Hola mundo
----------
La aplicación más sencilla que podemos crear:

Inclusión
#########
.. code-block:: Python
    :include: holamundo.py
    :start-at: #!/usr/bin/env python
    :end-before: # vista

Primero vamos a importar algunas herramientas para servir nuestro sitio de una manera autónoma.

wsgiref.simple_server:
    Es un servidor wsgi_ sencillo; que va a servir nuestro sitio.
pyramid.config:
    Nos va a permitir usar Configurator; para configurar nuestro pyramid.
pyramid.response:
    Módulo que se encarga de las respuestas a los requests.

.. raw:: pdf

    PageBreak oneColumn

Vista
#####
.. code-block:: Python
    :include: holamundo.py
    :start-at: # vista
    :end-before: # controlador

En Pyramid_, es posible declarar una función como vista. En este caso, se toma el request y se regresa una respuesta, la cual
concatena lo que pasemos de parámetro con la frase que vemos ahí.

.. Nota:: 
    matchdict_ es un método que regresará un objecto representando los parámetros.
   
.. raw:: pdf

    PageBreak oneColumn

Controlador
###########
.. code-block:: Python
    :include: holamundo.py
    :start-at: # controlador

Bueno, primero, instanciamos a Configurator_ y le agregamos la ruta llamada 'hola'; indicándole que todo lo que pongamos después de
'/hola/' será parámetros. La ruta será accesible en '/hole'.

Luego, agregamos la vista y se la asignamos a la ruta 'hola'.

Enseguida, instanciamos nuestra aplicación y se la pasamos al servidor para que la sirva; escuhando a todo el mundo; en el puerto
8080.

.. Advertencia::
    Usar la red 0.0.0.0 no es necesario cuando desarrollamos en privado. Es mejor usar 127.0.0.1 en esos casos.

Finalmente, iniciamos el servidor.

.. raw:: pdf

    PageBreak oneColumn

Completo
########
.. code-block:: Python
    :include: holamundo.py

Ahora, es muy fácil iniciar el servidor. Podemos hacer: 

.. code-block:: Bash

    chmod 700 ./holamundo.py
    ./holamundo

Ahora, podemos accesarlo en http://127.0.0.1:8080/hola/JuanchoDeLaCostilla.

.. raw:: pdf

    PageBreak oneColumn

Ejercicio
#########
Hacer el tutorial de: http://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/index.html


.. Links
.. _Configurator: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html?highlight=configurator#pyramid.config.Configurator
.. _FDL: http://www.gnu.org/licenses/fdl.txt
.. _Pyramid: http://pylonsproject.org/
.. _matchdict: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/request.html?highlight=matchdict#pyramid.request.Request.matchdict
.. _wsgi: https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

.. Directives
.. |version| date:: %Y%m%d
.. |year| date:: %Y

.. Settings
.. footer::
    Renich Bon Ciric | |year| | ###Title### - pag. ###Page###
