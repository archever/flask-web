# coding=utf-8
from config import PWD_SALT
from models.user import User
from libs.passwd import gen_passwd
from libs.errors import AppError


class UserCtr(object):

    def __init__(self, usermodel):
        self.email = usermodel.email
        self._status = usermodel.status

    @property
    def status(self):
        pass

    def to_dict(self):
        return

    @classmethod
    def login(cls, email, password):
        password = gen_passwd(password, PWD_SALT)
        user = User.select().where(User.email == email & User.password == password).first()
        if not user:
            raise AppError("用户名, 密码错误")
        return cls(user)

    @classmethod
    def regist(cls, email, password):
        password = gen_passwd(password, PWD_SALT)
        user = User.insert(User(email=email, password=password))
        return cls(user)
