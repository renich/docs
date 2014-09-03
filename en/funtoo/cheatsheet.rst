Description
===========
This is my main funtoo cheatsheet.

Emerge
------

.. code:: bash

    ## rebuild toolchain (everything?)
    emerge --sync && emerge -1 glibc && emerge -ajuNDv @world

Alternate version (hardened)

.. code:: bash

    # hardened version of rebuild everything
    # should select hardened profile first
    source /etc/profile
    emerge --oneshot gcc
    emerge --oneshot binutils virtual/libc
    emerge --depclean prelink
    emerge --emptytree --verbose @world
