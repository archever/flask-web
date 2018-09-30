# coding=utf-8


def b(data):
    if isinstance(data, bytes):
        return data
    if isinstance(data, str):
        return data.encode("utf-8")


def s(data):
    if isinstance(data, bytes):
        return data.decode("utf-8")
    if isinstance(data, str):
        return data.encode("utf-8")
