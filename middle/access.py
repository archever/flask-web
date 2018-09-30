# coding=utf-8
"""
请求日志
"""

import time
from flask import request, Blueprint
from libs.log import getLogger

log = getLogger('access')


def after_request_access(resp):
    """
    打印请求参数, 返回值, 请求时间
    """
    # 请求值
    content_type = request.headers.get('content-type', '')
    # 处理 body 为空 json 报错的问题
    if not request.content_length:
        req_data = request.data
    elif 'form' in content_type:
        req_data = dict(request.form)
    elif 'json' in content_type:
        req_data = dict(request.json)
    else:
        req_data = request.data

    req_time = 1000*(time.time()-request.req_start)

    # json 返回值
    if 'json' in resp.headers.get('content-type', ''):
        if req_data:
            log.info(
                '%s %s:%s %.2fms \ncookies: %s \nreq: %s \nresp: %s',
                resp.status_code,
                request.method, request.full_path,
                req_time, request.cookies, req_data, resp.data.decode('utf-8')
            )
        else:
            log.info(
                '%s %s:%s %.2fms \ncookies: %s \nresp: %s', resp.status_code,
                request.method, request.full_path, req_time, request.cookies, resp.data
            )
    # 非 json 返回值
    else:
        if req_data:
            log.info(
                '%s %s:%s %.2fms \ncookies: %s \nreq: %s', resp.status_code,
                request.method, request.full_path, req_time, request.cookies, req_data
            )
        else:
            log.info(
                '%s %s:%s %.2fms \ncookies: %s',
                resp.status_code, request.method, request.full_path, req_time,
                request.cookies)

    return resp


def before_request_access():
    """
    设置请求开始时间
    """
    request.req_start = time.time()


def log_error(err):
    """
    打印错误日志
    """
    if err:
        log.error(err, exc_info=err)
