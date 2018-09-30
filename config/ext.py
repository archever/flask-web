# coding=utf-8

import peewee as pw
import redis as redis_
from config import PG_HOST, PG_USER, PG_PWD

db = pw.PostgresqlDatabase('demo', **{'host': PG_HOST, 'user': PG_USER, 'password': PG_PWD})
redis = redis_.Redis()
