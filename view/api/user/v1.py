# coding=utf-8

from flask import Blueprint, request, session, jsonify
from libs.errors import AppError
from controlers.user import UserCtr

bp = Blueprint("user/v1", __name__, url_prefix="/api/user/v1")


@bp.route("login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        raise AppError("参数错误")

    user = UserCtr.login(email, password)
    sid = session.login(user)
    return jsonify(code=0, msg="", data={
        "sid": sid,
        "user": user.to_dict(),
    })
