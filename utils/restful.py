# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 19:53
from django.http import JsonResponse


class StatuCode(object):
    ok = 200
    error = 400
    internet_error = 500
    expire_error = 401
    not_exist = 404


def success(data=None, code=StatuCode.ok, msg="ok"):
    if data is None:
        data = {}
    return JsonResponse({"code": code, 'msg': msg, 'data': data})


def param_error(data=None, code=StatuCode.error, msg="error", error_type=""):
    if data is None:
        data = {}
    return JsonResponse({"code": code, 'msg': msg, 'data': data, 'error_type': error_type})


def server_error(code=StatuCode.internet_error, msg="internet error", data=None):
    return JsonResponse({"code": code, 'msg': msg, 'data': data})
