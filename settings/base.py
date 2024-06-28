"""
Django settings for django_miniprogram_template project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--4+t(-mrt+&_&tq5f*%0x%!_($-79b38_omun^8a8=e9nv_=5_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.mini_auth.MiniAuthMiddleware',
]

ROOT_URLCONF = 'django_miniprogram_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_miniprogram_template.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join('static'),)
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 配置日志系统
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {  # 格式化
        'simple': {  # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(filename)s[%(lineno)s] %(levelname)-2s %(message)s',
            'datefmt': "%Y-%m-%d %X",
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # 控制台输出
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'info_logger.log'),
        },
        'performance': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'performance_log.log'),
        },
    },
    'loggers': {
        "info_logger": {
            "handlers": ["file"],
            "level": "INFO",
        },
        "error_logger": {
            "handlers": ["file"],
            "level": "ERROR",
        },
    },
}

info_logger = logging.getLogger("info_logger")
error_logger = logging.getLogger("error_logger")