# -*- coding: utf-8 -*-
"""
Author : donghao
Time   : 2021/3/9 8:44 下午
"""

from __future__ import absolute_import
from django.db import models


class ModelBase(models.Model):
    """
    基类
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta(object):
        abstract = True
        managed = False
