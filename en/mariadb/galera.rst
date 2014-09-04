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
    * node1
    * node2
    * node3

client1:
    Consumes the DB provided by the cluster.
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

Please, do the following for all our servers: client, node1, node2 and node3.

.. code-block:: Bash

    cat < 'EOF' >> /etc/hosts

    # Private network
    10.0.0.10 client.privatelan client
    10.0.0.129 node1.privatelan node1
    10.0.0.130 node2.privatelan node2
    10.0.0.131 node3.privatelan node3
    EOF

.. Important:: 
    Please, consider using DNS instead of /etc/hosts for production/development environments. /etc/hosts is hard to
    maintain. (unless you're ussing salt)
    

client
------
.. code-block:: Bash

    # become root
    su -

    # install haproxy and mariadb client
    yum -y install haproxy mariadb

    # create directory for haproxy in /run
    cat < 'EOF' > /etc/tmpfiles.d/haproxy.conf
    d /run/haproxy 755 root root  -
    EOF

    systemd-tmpfiles --create

    # configuration
    cat < 'EOF' > /etc/haproxy/haproxy.cfg
    global
        chroot /var/lib/haproxy
        daemon
        group haproxy
        log 127.0.0.1 local2
        maxconn 1024
        pidfile /var/run/haproxy.pid
        stats socket /var/lib/haproxy/stats
        user haproxy

    defaults
        mode http
        log global
        option tcplog
        option dontlognull
        option redispatch
        retries 3
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms
        maxconn 1024

    listen mariadb-cluster
        mode tcp
        bind unix@/run/haproxy/mariadb-cluster.sock
        balance leastconn
        option mysql-check user haproxy
        server node1 10.0.0.129:3306 check
        server node2 10.0.0.130:3306 check
        server node3 10.0.0.131:3306 check

    listen stats 127.0.0.1:9000
        mode http
        stats enable
        stats uri /haproxy_stats
        stats realm HAProxy\ Statistics
        stats auth haproxy:haproxy
        stats admin if TRUE
    EOF

    # edit /etc/my.cnf so that we use our cluster socket as a default
    sed -ri 's@socket=/var/lib/mysql/mysql.sock@socket=/run/haproxy/mariadb-cluster.sock@' /etc/my.cnf

    # enable it
    systemctl enable haproxy.service

    # start it
    systemctl enable haproxy.service


node{1..3}
----------
Ok, work done here has to be interpreted. Please, interpolate whatever is necessary. 

Also, I recommend using clusterssh for the job. It is much simpler to do it that way. You might prefer salt or ansible.

.. code-block:: Bash
    
    # become root
    su -

    # install galera
    yum -y install mariadb-galera-server

    # configure
    cat < 'EOF' > /etc/my.cnf.d/galera.cnf
    [mysqld]
    binlog_format="ROW"
    default-storage-engine="innodb"
    innodb_autoinc_lock_mode=2
    innodb_locks_unsafe_for_binlog=1
    query_cache_size=0
    query_cache_type=0
    bind-address="10.0.0.0/24"
    wsrep_provider="/usr/lib64/galera/libgalera_smm.so"
    #wsrep_provider_options=""
    wsrep_cluster_name="mariadb-cluster"
    wsrep_cluster_address="gcomm://node1,node2,node3"
    wsrep_node_name="node1" # change this per node
    wsrep_node_address="10.0.0.129" # change this per node
    wsrep_slave_threads=1
    wsrep_certify_nonPK=1
    wsrep_max_ws_rows=131072
    wsrep_max_ws_size=1073741824
    wsrep_debug=0
    wsrep_convert_LOCK_to_trx=0
    wsrep_retry_autocommit=1
    wsrep_auto_increment_control=1
    wsrep_drupal_282555_workaround=0
    wsrep_causal_reads=0
    wsrep_notify_cmd=""
    wsrep_sst_method="rsync"
    wsrep_sst_receive_address="10.0.0.129" # change this per node
    EOF

    # enable
    systemctl enable mariadb.service

    # start cluster (huh?)
    #systemctl start mariadb.service # does not work to start the cluster

 
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
