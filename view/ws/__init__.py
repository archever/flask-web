# codiing=utf-8
import logging
from flask import Blueprint, request, abort, g

bp = Blueprint("ws", __name__, url_prefix="/ws")
log = logging.getLogger(__name__)


@bp.before_request
def ensure_ws():
    ws = request.environ.get('wsgi.websocket')
    if not ws:
        return abort(400)
    g.ws = ws


@bp.route("")
def index():
    ws = g.ws
    while True:
        message = ws.receive()
        if message is None:
            break
        log.debug("message: %s", message)
        ws.send(message)
    ws.close()
    return "", 203
