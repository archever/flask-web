# coding=utf-8

import os
from flask import Flask
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from gevent import monkey
import config
monkey.patch_all()

from config import PORT, HOST
from libs.session import RedisSessionInterface
from middle.access import after_request_access, before_request_access, log_error


def create_app():
    app = Flask("flask-web")
    app.session_interface = RedisSessionInterface()
    app.config.from_object(config)

    # middle
    from middle.errors import bp
    app.register_blueprint(bp)
    app.before_request(before_request_access)
    app.after_request(after_request_access)
    app.teardown_request(log_error)

    # view
    from view.index import bp
    app.register_blueprint(bp)
    from view.ws import bp
    app.register_blueprint(bp)
    from view.api.user.v1 import bp
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    app = create_app()
    print("listen on %s:%s" % (HOST, PORT))
    http_server = WSGIServer((HOST, PORT), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
