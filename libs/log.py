# coding=utf-8

import logging
import sys
from colorlog import ColoredFormatter


def init_log(log_dir, log_level, opt):
    """
    :param str log_dir: 
    :param logging.DEBUG|... log_level: 
    :param list opt: [
        ('requests', logging.WARN),
        ('werkzeug', logging.WARN),
        ('sqlalchemy', logging.WARN),
        ('sqlalchemy.engine.base.Engine', logging.WARN),
        ('PIL', logging.WARN),
    ]
    """
    if log_dir:
        ch = logging.handlers.RotatingFileHandler(
            '{}/{}_app.log'.format(log_path, app.name), 'w',
            10 * 1024 * 1024, 20)
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
