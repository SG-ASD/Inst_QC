from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wkv0eo^r-u#aneynu^*y1j08e4r2c)(#jh9_163)5ilctaqw-e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Inst_QC_local',
        'USER': 'root',
        'PASSWORD': 'mariadb',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}