"""
Django settings for twitter_chat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOGIN_URL = "/login"
LOGOUT_URL = "/"
LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cycv^&6x=#k&0^4#a)@4gur9j*c^k*d4tb@r#5-kze-+sexm6@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sslserver',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASE_OPTIONS = {'use_unicode': False, 'charset': 'utf8'}

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'tchat',
    'USER': 'psql',
    'PASSWORD': '123qwe',
    'HOST': 'localhost',
    'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "twitter_chat", "static", "templates"),
)

if DEBUG:
    MEDIA_URL = '/media/'
    print os.path.join(os.path.dirname(BASE_DIR), "static", "twitter_chat", "templates"),
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "twitter_chat", "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "twitter_chat", "static", "templates")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "twitter_chat", "static"),
        os.path.join(os.path.dirname(BASE_DIR), "twitter_chat", "static", "bootstrap"),
    )
