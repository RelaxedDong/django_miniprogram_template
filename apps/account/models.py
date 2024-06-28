from django.db import models

from apps.account.consts import UserGenderEnum
from apps.consts import StatusEnum
from apps.models import ModelBase
from django.utils import timezone


# Create your models here.
class AccountModel(ModelBase):
    openid = models.CharField("open id", max_length=50, unique=True, default=None, blank=True, null=True)
    nickname = models.CharField("微信昵称", max_length=50)
    avatar_url = models.CharField('头像', max_length=255, blank=True)
    country = models.CharField('国家', max_length=30, blank=True)
    province = models.CharField('省份', max_length=30, blank=True)
    city = models.CharField('城市', max_length=30, blank=True)
    gender = models.CharField("性别", choices=UserGenderEnum, default=UserGenderEnum.UNKNOW, max_length=1)
    status = models.CharField('状态', max_length=1, choices=StatusEnum, default=StatusEnum.NORMAL)
    last_login = models.DateTimeField("上次登陆", default=timezone.now, null=False, blank=False)
    phone = models.CharField("手机号", null=False, blank=False, max_length=11)
    wechat = models.CharField("微信号", null=True, blank=True, max_length=50)
    session_key = models.CharField("session_key", max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'account'
        verbose_name = '小程序用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.nickname, self.phone)
