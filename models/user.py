
from peewee import *
from config.ext import db as database


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    email = CharField()
    id = IntegerField(constraints=[SQL("DEFAULT nextval('user_id_seq'::regclass)")])
    nick = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sid = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'user'
        primary_key = False
