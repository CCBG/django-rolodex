"""
Django settings for django_example project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%w1)bj+9ehivnvqjv=sal*y(wiwwz5y!m@v1zeracm&5)e%xp%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Brugger: Uncomment for production use, and the setting will change below 
#DEBUG = False



ALLOWED_HOSTS = []

if ( DEBUG == False):
    ALLOWED_HOSTS = ['rolodex.ctrulab.uk']


# Application definition

INSTALLED_APPS = [
    'rolodex',          # The apps we are developing
    'widget_tweaks', # Makes rendering forms a lot easier
    'debug_toolbar', # Awesome for debugging django sites
    # Standard stuff
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'rolodex_db':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'rolodex_db.sqlite3'),
    },
}

DATABASE_ROUTERS = ['django_example.router.Router']

if ( DEBUG == False ):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'rolodex_django',
            'USER': 'easih_admin',
            'PASSWORD': 'easih',
            'HOST': 'mgsrv01',
            },

        'vmail_db': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'rolodex',
            'USER': 'easih_admin',
            'PASSWORD': 'easih',
            'HOST': 'mgsrv01',
            },
        }




# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_ROOT      = os.path.join(BASE_DIR, 'static')
# This is for the dev static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_dev')]



STATIC_URL = '/static/'
