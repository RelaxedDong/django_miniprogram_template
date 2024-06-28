# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/28 10:58 AM
@Auth ： donghao
"""
from common_tool.enum import EnumBase, EnumItem


class UserGenderEnum(EnumBase):
    UNKNOW = EnumItem('0', '未知')
    MALE = EnumItem('1', '男')
    FEMEALE = EnumItem('2', '女')
