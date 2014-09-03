Pyramid
=======
Este es un HowTo básico para Pyramid_.

Está diseñado, el artículo, como para generar un PDF y que pueda ser distribuido en forma impresa. 

Para generar el PDF, es necesario instalar rst2pdf_.

.. code-block:: Bash

    # En Fedora
    su -c 'yum -y install rst2pdf'

Una vez instalado, usa el comando:

.. code-block:: Bash

    make

Se generará un PDF y es fácil de imprimir, enviar o ver de cualquier manera. Además, ahí si se muestran bien los ejemplos; no como
en Github.


.. Links
.. _Pyramid: http://www.pylonsproject.org/
.. _rst2pdf: https://code.google.com/p/rst2pdf/
