# coding=utf-8

import sys
import logging
import logging.handlers
from colorlog import ColoredFormatter
from config import LOG_DIR, LOG_LEVEL

_inited = False
app_name = 'demo'
opt = [
    ('requests', logging.WARN),
    ('werkzeug', logging.WARN),
    ('PIL', logging.WARN),
    ('raven.base.Client', logging.WARN),
    ('geventwebsocket.handler', logging.WARN),
]


def init_log(opt=None):
    global _inited
    if _inited:
        return
    _inited = True
    if not opt:
        opt = []
    log_level = LOG_LEVEL
    log_path = LOG_DIR

    if log_path:
        ch = logging.handlers.RotatingFileHandler(
            '{}/{}_app.log'.format(log_path, app_name), 'w', 10 * 1024 * 1024, 20)
    else:
        ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(ColoredFormatter(
        '%(log_color)s[%(levelname)1.1s %(asctime).19s %(name)s:%(lineno)d] %(white)s%(message)s',
        log_colors={
            'DEBUG': 'blue',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_blue'
        }
    ))
    logging.root.setLevel(log_level)
    logging.root.addHandler(ch)
    for logger, level in opt:
        log = logging.getLogger(logger)
        log.setLevel(level)
        log.addHandler(logging.NullHandler(level=logging.WARN))


def getLogger(name):
    global opt
    init_log(opt)
    return logging.getLogger(name)
