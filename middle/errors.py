# coding=utf-8

from flask import jsonify, request, render_template
from libs.errors import AppError
from libs.log import getLogger
from flask import Blueprint

bp = Blueprint('errors', __name__)
log = getLogger(__name__)


@bp.app_errorhandler(AppError)
def internal_error(e):
    log.error(e, exc_info=e)
    return jsonify(success=False, msg=e.messsage), e.http_code


@bp.app_errorhandler(Exception)
def exception_error(e):
    log.error(e, exc_info=e)
    return jsonify(success=False, msg='oops'), 500


@bp.app_errorhandler(400)
@bp.app_errorhandler(401)
@bp.app_errorhandler(403)
@bp.app_errorhandler(404)
@bp.app_errorhandler(405)
@bp.app_errorhandler(410)
@bp.app_errorhandler(429)
@bp.app_errorhandler(503)
def not_found(e):
    if '/api/' in request.path:
        return jsonify(success=False, errno=e.code, msg=e.description), e.code
    return render_template('error.html', msg=e.description), e.code
