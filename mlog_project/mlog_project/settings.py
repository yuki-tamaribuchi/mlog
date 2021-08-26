"""
Django settings for mlog_project project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

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
DEBUG = os.environ.get('MLOG_DEBUG_STATE', False)

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
    'django_select2',
    'django_nose',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    'sslserver',
    'debug_toolbar',
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
                'csp.context_processors.nonce'
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
        'NAME': 'mlog_project_db',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.User'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MLOG_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('MLOG_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'


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


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.environ.get('MLOG_OAUTH_GOOGLE_CLIENT_ID'),
            'secret': os.environ.get('MLOG_OAUTH_GOOGLE_SECRET'),
            'key': os.environ.get('MLOG_OAUTH_GOOGLE_KEY')
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIALACCOUNT_ADAPTER = 'accounts.adapter.MySocialAccountAdapter'


ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_FORMS = {
    'signup' : 'accounts.forms.SignupForm',
}


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
]
CSP_STYLE_SRC = [
    "'self'",
    "'unsafe-inline'",
    "https://stackpath.bootstrapcdn.com",
    "https://cdn.jsdelivr.net",
    "https://cdnjs.cloudflare.com",
    ]
CSP_IMG_SRC = [
    "'self'",
    "https://storage.googleapis.com",
    "https://i.scdn.co",
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