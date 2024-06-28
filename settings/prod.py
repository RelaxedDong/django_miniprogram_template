# -*- coding: utf-8 -*-
"""
# 上产环境
@Time ： 2024/6/28 11:22 AM
@Auth ： donghao
"""
from settings.base import *

# 小程序相关配置
WX_MINI_SETTINGS = {
    'APP_ID': "",
    'APP_SECRET': "",
}


DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "www.xxx.cn"]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {'CLIENT_CLASS': 'django_redis.client.DefaultClient'}
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_miniprogram_template',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0",
            "charset": 'utf8mb4'
        }
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
