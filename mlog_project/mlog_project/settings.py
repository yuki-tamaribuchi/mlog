"""
Django settings for mlog_project project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# default secret key was generated by Djecrety. https://djecrety.ir/
SECRET_KEY = os.environ.get('MLOG_SECRET_KEY', 'peebiyrn+1_yed4%ukd_leqzg35fk1jla)of+ns44m9i_efy5_')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if (os.environ.get('MLOG_DEBUG_STATE'))=='True' else False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',


    'accounts',
    'mlog',
    'search',
    'comments',
    'likes',
    'favorite_artists',
    'follow',
    'activity',
    'musics',
    'entry',
    'notifications',
    'contacts',

    
    'django_select2',
    'django_nose',
    'sslserver',
    'debug_toolbar',
    'storages',
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mlog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'csp.context_processors.nonce',
                'notifications.context_processors.unread_notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'mlog_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES_LIST = {
    'main': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mlog_db',
        'USER': os.environ.get('MLOG_DB_USER'),
        'PASSWORD': os.environ.get('MLOG_DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    },
    'docker':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mlog_db',
        'USER': 'mlog_db_user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

DATABASES={}
default_database = os.environ.get('DJANGO_DATABASE', 'main')
DATABASES['default'] = DATABASES_LIST[default_database]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = [
    ('en', _('English')),
    ('ja', _('Japanese')),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


USE_S3 = True if (os.environ.get('MLOG_USE_S3')=='True') else False

if USE_S3:
    AWS_ACCESS_KEY_ID = os.environ.get('MLOG_AWS_S3_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('MLOG_AWS_S3_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('MLOG_AWS_S3_STORAGE_BUCKET_NAME')

    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'mlog_project.storage_backends.PublicMediaStorage'
else:
    STATIC_URL = '/staticfiles/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/mediafiles/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.User'


EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_ACCESS_KEY_ID = os.environ.get('MLOG_AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('MLOG_AWS_SES_SECRET_ACCESS_KEY')

AWS_SES_REGION_NAME = 'ap-northeast-1'
AWS_SES_REGION_ENDPOINT = 'email.ap-northeast-1.amazonaws.com'
DEFAULT_FROM_EMAIL = os.environ.get('MLOG_DEFAULT_FROM_EMAIL')


CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'select2_local':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://127.0.0.1:6379/2',
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    },
    'select2_docker':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://redis:6379/2',
        'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    }
}

CACHES['select2']=CACHES[os.environ.get('SELECT2_DEFAULT','select2_local')]

SELECT2_CACHE_BACKEND='select2'


LOGIN_REDIRECT_URL = 'mlog:timeline'

CELERY_BROKER_URLS={
    'local':"redis://127.0.0.1:6379/1",
    'docker':"redis://redis:6379"
}

CELERY_BROKER_URL = CELERY_BROKER_URLS[os.environ.get('CELERY_BROKER_DEFAULT','local')]

CELERY_RESULT_BACKENDS={
    'local':"redis://127.0.0.1:6379",
    'docker':"redis://redis:6379"
}

CELERY_RESULT_BACKEND = CELERY_RESULT_BACKENDS[os.environ.get('CELERY_RESULT_BACKENDS_DEFAULT','local')]

CELERY_TIMEZONE = "Asia/Tokyo"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60


#Setting for django-nose
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS_LIST = {
    'local':{
        '--with-xunit',
        '--xunit-file=result/unittest.xml',
    },
    'docker':{
        '--with-xunit',
        '--xunit-file=mlog_project/result/unittest.xml',
    }
}

nose_args_selection = os.environ.get('NOSE_ARGS_SELECTION', 'local')
NOSE_ARGS = NOSE_ARGS_LIST[nose_args_selection]


CSP_DEFAULT_SRC = [
    "'self'",
    "https://ka-f.fontawesome.com",
    "https://p.scdn.co",
    ]
CSP_SCRIPT_SRC = [
    "'self'",
    "https://code.jquery.com",
    "https://stackpath.bootstrapcdn.com",
    "https://cdnjs.cloudflare.com",
    "https://cdn.jsdelivr.net",
    "https://kit.fontawesome.com",
    "https://mlog-s3.s3.amazonaws.com",
]
CSP_STYLE_SRC = [
    "'self'",
    "'unsafe-inline'",
    "https://stackpath.bootstrapcdn.com",
    "https://cdn.jsdelivr.net",
    "https://cdnjs.cloudflare.com",
    "https://mlog-s3.s3.amazonaws.com",
    ]
CSP_IMG_SRC = [
    "'self'",
    "https://storage.googleapis.com",
    "https://i.scdn.co",
    "https://mlog-s3.s3.amazonaws.com",
]
CSP_FONT_SRC = [
    "'self'",
    "https://cdnjs.cloudflare.com",
    "https://ka-f.fontawesome.com",
]
CSP_FRAME_SRC = [
    "https://*.spotify.com",
]

CSP_MEDIA_SRC = [
    "https://p.scdn.co",
]


SPOTIFY_CLIENT_ID = os.environ.get('MLOG_SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('MLOG_SPOTIFY_CLIENT_SECRET')


INTERNAL_IPS = [
    '127.0.0.1',
]