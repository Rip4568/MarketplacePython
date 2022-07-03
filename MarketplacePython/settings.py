"""
Django settings for MarketplacePython project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import django_on_heroku
from dotenv import load_dotenv
load_dotenv()
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))#resolvendo o problema de TemplateDoesNotExists

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-jumo4esalf_x+bj$w&0r@khmon3)rp3onr8_@zszr!=e$76!(y'
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False

DEBUG = os.getenv('DEBUG',default=False) == 'True'

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #installed apps 3rd party
    'debug_toolbar',
    'widget_tweaks',
    'crispy_forms',
    'localflavor',
    #'cloudinary_storage',antes de testar o cloudinary ver o funcionamento do whitenoise
    #'cloudinary',
    #'Users_app',
    'Users_app.apps.UsersAppConfig',
    'Pages_app.apps.PagesAppConfig',
    'Produtos_app.apps.ProdutosAppConfig',
    'Cart_app.apps.CartAppConfig',
    'Ordens_app.apps.OrdensAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",#adicionado manualmente
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'MarketplacePython.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [ BASE_DIR / 'templates'],
        'DIRS': [ os.path.join(BASE_DIR , 'templates')],
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

WSGI_APPLICATION = 'MarketplacePython.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


""" Configuração padrão para acessar
o banco de dados do postgres """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES['default'] = dj_database_url.config()#mandar somente quando for upar pro heroku



"""

    if (teste) {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    } else {
        'ENGINE': 'django.db.backends.postgresql',#padrão .postgresql_psycopg2
        'NAME': 'db_MarketplacePython',#nome do banco de dados criado
        'USER': 'postgres',#padrão
        'PASSWORD': 'admin',#senha criada
        'HOST': 'localhost',#padrão
        'PORT': '5432',#padrão
        }    
    }
      
"""

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# User model (modelo de usuario padrão será oque eu construi no models.py e forms.py)
AUTH_USER_MODEL = 'Users_app.User'

#configuração dos arquivos a serem salvos

#MEDIA_URL = '/media/'
MEDIA_URL = '/static/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
MEDIA_ROOT = 'staticfiles/media/'

#testar o o salvamento dos arquivos na pasta static
STATICFILES_DIRS  = [
    os.path.join(BASE_DIR,'static/')
]

import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]


#Configurações do cart
CART_SESSION_ID = "cart"
CART_ITEM_MAX_QUANTITY = 5

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"#armazenados em cache para sempre e suporte a compactação

django_on_heroku.settings(locals())#resolvendo o problema do pytest