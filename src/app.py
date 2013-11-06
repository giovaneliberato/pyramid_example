import sys
from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def main():
    sys.path.append('../*')
    config = Configurator()
    config.include('pyramid_chameleon')
    config.scan("web.views")
    config.add_static_view('static', 'web/templates/static')
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
