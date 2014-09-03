#!/usr/bin/env python

# includes
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# vista
def hola_mundo( request ):
    return Response( 'Hola %(susodicho)s!' % request.matchdict )

# controlador
if __name__ == '__main__':
    config = Configurator()
    config.add_route( 'hola', '/hola/{susodicho}' )
    config.add_view( hola_mundo, route_name='hola' )

    app = config.make_wsgi_app()
    server = make_server( '0.0.0.0', 8080, app )
    server.serve_forever()
