# coding=utf-8
import os
import logging
from flask import Flask
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from gevent import monkey
monkey.patch_all()

from config import PORT, LOG_DIR, LOG_LEVEL, HOST
from libs.log import init_log
from middle.access import before_request_access, after_request_access, log_error

init_log(LOG_DIR, LOG_LEVEL, [
    ('requests', logging.WARN),
    ('werkzeug', logging.WARN),
    ('geventwebsocket.handler', logging.WARN),
])

app = Flask("flask-web")
app.before_request(before_request_access)
app.after_request(after_request_access)
app.teardown_request(log_error)

from view.index import bp
app.register_blueprint(bp)
from view.api.user.v1 import bp
app.register_blueprint(bp)
from view.ws import bp
app.register_blueprint(bp)

if __name__ == "__main__":
    http_server = WSGIServer((HOST, PORT), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
