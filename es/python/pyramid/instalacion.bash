# instalar python3
su -c 'yum install python3 python3-dev'

# generar ambiente virtual
pyvenv ~/pyramid

# entrar/activar el ambiente virtual
cd ~/pyramid
source ./bin/activate

# instalar setuptools en el ambiente virtual
curl https://bootstrap.pypa.io/ez_setup.py | python

# instalar pip
easy_install pip

# instalar Pyramid
easy_install 'pyramid==1.5.1'
