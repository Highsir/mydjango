"""
Django settings for myDjango project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aic0x4%1_beg6_bct^0(l97v=&%pxgpi4_ks&_cmko*o2r2l=!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# AUTH_USER_MODEL = "users.User"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'index',
    "mydefined",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myDjango.urls'

TEMPLATES = [
    #  使用Jinja2模板引擎
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'myDjango.jinja2.environment',
        },
    },
    # 使用Django模板引擎
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'myDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'mydjango',
         'USER': 'root',
         'PASSWORD': '123456',
         'HOST': '127.0.0.1',
         'PORT': '3306',
     },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mydjango',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     },
#     'db1':{
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'indexdb',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         },
#     "db2":{
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'userdb',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
# DATABASE_ROUTERS = ['myDjango.db_router.dbAppsRouter']
# DATABASE_APPS_MAPPING = {
#     'admin': 'default',
#     'index': 'db1',
#     'user': 'db2',
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/Allstatic/'
STARICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'index/Mystatic')]

MEDIA_URL = '/media/'
MEDIA_ROOT = [os.path.join(BASE_DIR, 'media')]

# 自定义COOKIE加密
SIGNING_BACKEND = 'myDjango.signer.myTimestampSigner'

# 配置文件数据的临时存放文件夹
FILE_UPLOAD_TEMP_DIR = '/tmp'
FILE_UPLOAD_MAX_MEMORY_SIZE = 209715200
FILE_UPLOAD_HANDLERS = ['myDjango.handler.myFileUploadHandler']