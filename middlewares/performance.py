# -*- coding: utf-8 -*-
"""
日志中间价
Author : donghao
Time   : 2021/7/31 8:04 下午
"""

from __future__ import absolute_import

import time

from common_tool.http import get_post_data, get_ip_from_request
from common_tool.loggers import performance_logger


class PerformanceLoggerMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def get_get_or_post_data(self, request):
        if request.method == "GET":
            return request.GET.dict()
        return get_post_data(request)

    def __call__(self, request):
        # 视图函数执行前的代码
        start = time.time()
        response = self.get_response(request)
        # 视图函数执行后的代码
        spend_time = time.time() - start
        ip = get_ip_from_request(request)
        data = self.get_get_or_post_data(request)
        # response['duration-ms'] = t
        performance_logger.info(
            "[%s][%s] [%s] [%s]  %s" % (request.method, '%.3f' % spend_time, ip, request.path, data))
        return response
