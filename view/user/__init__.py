# coding=utf-8
from flask import Blueprint, render_template, redirect
from controlers.user import UserCtr
from libs.login import login_user, logout_user, current_user

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/login", methods=["GET"])
def login_form():
    return render_template("user/login.html")


@bp.route("/regist", methods=["GET"])
def regist_form():
    return render_template("user/regist.html")


@bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect("/")


@bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        raise AppError("参数错误")

    user = UserCtr.login(email, password)
    user.sid = login_user(user)
    return redirect("/")


@bp.route("/regist", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        raise AppError("参数错误")

    user = UserCtr.regist(email, password)
    sid = session.login(user)
    return redirect("/")
