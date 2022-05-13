from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}

DEBUG = False

ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = 'config.wsgi.deploy.application'