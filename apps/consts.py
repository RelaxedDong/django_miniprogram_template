# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/28 10:58 AM
@Auth ： donghao
"""
from common_tool.enum import EnumBase, EnumItem


class StatusEnum(EnumBase):
    DELETED = EnumItem('0', '删除')
    NORMAL = EnumItem('1', '正常')
