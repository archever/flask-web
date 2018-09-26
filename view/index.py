# coding=utf-8
from flask import Blueprint, render_template, redirect

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/user/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        raise AppError("参数错误")

    user = UserCtr.login(email, password)
    sid = session.login(user)
    return redirect("/")


@bp.route("/demo/ws")
def demo_ws():
    return render_template("ws.html")


@bp.route("/demo/todo")
def demo_todo():
    return render_template("todo.html")
