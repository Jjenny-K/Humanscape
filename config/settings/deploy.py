from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
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