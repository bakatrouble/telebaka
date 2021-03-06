import os
import environ

from bots.utils import get_plugins

root = environ.Path(__file__) - 2
env = environ.Env()

env_file = str(root.path('.env'))
if os.path.exists(env_file):
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)

DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_celery_results',
    'django_celery_beat',
    'dynamic_preferences',
    'django_extensions',
    'adminsortable2',
    'raven.contrib.django.raven_compat',
] + list(get_plugins().keys()) + [
    'bots.apps.BotsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'telebaka.urls'

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

WSGI_APPLICATION = 'telebaka.wsgi.application'

DATABASES = {
    'default': env.db('DATABASE_URL', 'sqlite:///db.sqlite3'),
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

public_root = root.path('public/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = 'media/'
STATIC_ROOT = public_root('static')
STATIC_URL = '/static/'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'redis://'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_WORKER_CONCURRENCY = 4

WEBHOOK_DOMAIN = env.url('WEBHOOK_DOMAIN', 'home.bakatrouble.pw').geturl()

RAVEN_CONFIG = {
    'dsn': env.str('SENTRY_DSN', None),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'sentry': {
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'level': 'WARNING',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'telegram.ext.dispatcher': {
            'handlers': ['console'] if DEBUG else ['console', 'sentry'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
