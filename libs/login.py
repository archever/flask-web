# coding=utf-8

from flask import session
from functools import wraps
from libs.errors import AppError
from config import redis
from controlers.user import UserCtr


def login(uid, exp=None):
    """
    登录
    :param int exp: 登录过期时间 seconds
    """
    session["uid"] = uid
    if exp:
        session.exp = exp
    return session.sid


def current_user():
    uid = session.get("uid")
    if not uid:
        raise AppError("用户未登录, 或者登录过期")
    return UserCtr.get(uid)


def is_login():
    return bool(session.get("uid"))


def logout_user():
    if session.get("uid"):
        del session["uid"]


def login_required(func):
    """
    登录需求装饰器
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not is_login():
            raise AppError('用户未登录, 或登录过期')
        return func(*args, **kwargs)
    return decorated_view
