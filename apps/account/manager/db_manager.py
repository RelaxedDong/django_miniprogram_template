# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/28 11:04 AM
@Auth ： donghao
"""

from apps.account.models import AccountModel


def get_user_by_openid_safe(openid):
    if not openid:
        return None
    try:
        return AccountModel.objects.get(openid=openid)
    except:
        return None


def update_user_info(user, nickname='', avatar_url='', wechat='', phone='', age='', gender='', session_key="",
                     last_login=""):
    if nickname:
        user.nickname = nickname
    if avatar_url:
        user.avatar_url = avatar_url
    if wechat:
        user.wechat = wechat
    if phone:
        user.phone = phone
    if age:
        user.age = age
    if gender:
        user.gender = gender
    if session_key:
        user.session_key = session_key
    if last_login:
        user.last_login = last_login
    user.save()


