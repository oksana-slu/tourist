from local_settings import *
import os

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__) + '/', '../')) + '/'
LIB_PATH = os.path.join(PROJECT_ROOT, 'libs')


TIME_ZONE = 'America/Chicago'
#LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = PROJECT_ROOT + 'media/'
MEDIA_URL = '/s/'
ADMIN_MEDIA_PREFIX = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "dj_site.context_processors.site_url",
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'dj_site.urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT + "dj_site/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'dj_site.xtclass',
    'dj_site.xtobject',
    'dj_site.xtlink',
    'dj_site.xttopic',
    )
