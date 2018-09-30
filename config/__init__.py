# coding=utf-8

import os
import logging
from dotenv import load_dotenv
load_dotenv(".env")

# const
PORT = int(os.getenv("PORT", "6000"))
LOG_DIR = os.getenv("LOG_DIR", "")
LOG_LEVEL = getattr(logging, os.getenv("LOG_LEVEL", "DEBUG"))
HOST = os.getenv("HOST", "127.0.0.1")
PWD_SALT = os.getenv("PWD_SALT", "pqwoeiruty")
PG_HOST = os.getenv("PG_HOST", "127.0.0.1")
PG_USER = os.getenv("PG_USER", "demo")
PG_PWD = os.getenv("PG_USER", "demo")
TESTING = os.getenv("TESTING", "True")
DEBUG = os.getenv("TESTING", "True")
