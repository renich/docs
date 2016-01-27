=======
ebuilds
=======
--------------------
How to build ebuilds
--------------------

Updating your ebuild
====================
Just issue:

.. code::bash

    # go to your ebuild
    cd /usr/local/portage/media-sound/bitwig-studio
    cp bitwig-studio-1.3.5.ebuild bitwig-studio-1.3.6.ebuild
    ebuild bitwig-studio-1.3.6.ebuild digest

    # install it
    su -c 'emerge bitwig-studio'
