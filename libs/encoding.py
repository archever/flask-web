# coding=utf-8


def b(data):
    if isinstance(data, bytes):
        return b
    if isinstance(data, str):
        return str.encode("utf-8")
