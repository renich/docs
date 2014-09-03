=================================
HowTo: MariaDB + Galera + HAProxy
=================================
------------------------------------------------
Configure a highly available cluster with Galera
------------------------------------------------

:Author: 
    Renich Bon Ciric <renich@woralelandia.com>

:License: 
    FDL_ 1.3 o >

:Version:
    20140903

.. raw:: pdf

    PageBreak oneColumn

.. contents::

.. section-numbering::

.. raw:: pdf

    PageBreak oneColumn


Description
===========
This HowTo outlines how to make a minimal MariaDB_ + Galera_ installation; using HAProxy_.

The infrastructure is as it follows:

    * client
    * haproxy1
    * node1
    * node2
    * node3

client1:
    Consumes the DB provided by the cluster.
haproxy1:
    Balancer.
node{1..3}:
    Members of the cluster.

client has two NICs:

eth0:
    Public (Internet)
eth1:
    Private LAN

The rest are only part of the private network.


Requirerements
==============
* Fedora 20
* mariadb-galera
* haproxy


Procedure
=========

Networking
----------
We will be using the *10.0.0.1* network for the eth1 interface. 

To simplify the example, we will use /etc/hosts to map our cluster members and helpers to friendly names. That said, I will always
prefer DNS over /etc/hosts.

Please, do the following for all our servers: haproxy1, node1, node2, node3 and client.

.. code-block:: Bash

    cat << 'EOF' >> /etc/hosts

    # Private network
    10.0.0.10   client.privatelan client
    10.0.0.129  haproxy1.privatelan haproxy1
    10.0.0.130  node1.privatelan node1
    10.0.0.131  node2.privatelan node2
    10.0.0.132  node3.privatelan node3
    EOF

.. Important:: 
    Please, consider using DNS instead of /etc/hosts for production/development environments. /etc/hosts is hard to
    maintain. (unless you're ussing salt)
    

haproxy1
--------
.. code-block:: Bash

    # become root
    su -

    # install haproxy
    yum -y install haproxy

    # enable it
    systemctl enable haproxy.service

    # start it
    systemctl enable haproxy.service


node{1..3}
----------
Ok, work done here has to be interpreted. Please, interpolate whatever is necessary. 

.. code-block:: Bash
    
    

        
Troubleshooting
===============


Reference
=========


.. Links
.. _FDL: https://www.gnu.org/licenses/fdl.txt
.. _Galera: http://galeracluster.com/
.. _HAProxy: http://www.haproxy.org/
.. _MariaDB: https://mariadb.org/

.. Directives
.. |year| date:: %Y

.. Settings
.. footer::
    Renich Bon Ciric | |year| | ###Title### - p. ###Page###
