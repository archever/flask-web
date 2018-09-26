# coding=utf-8
from hashlib import sha1
from libs.encoding import b


def gen_passwd(passwd, salt):
    return sha1(b(passwd + salt)).hexdigest()
