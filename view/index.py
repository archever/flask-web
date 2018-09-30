# coding=utf-8
from flask import Blueprint, render_template, redirect, current_app, jsonify

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/url_map")
def url_map():
    """
    路由列表
    """
    data = []
    for i in list(current_app.url_map.iter_rules()):
        data.append({
            'rule': i.rule,
            'endpoint': i.endpoint,
        })
    return jsonify(success=True, data=data)


@bp.route("/demo/ws")
def demo_ws():
    return render_template("ws.html")


@bp.route("/demo/todo")
def demo_todo():
    return render_template("todo.html")
