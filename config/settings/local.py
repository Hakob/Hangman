from decouple import Config, RepositoryEnv

from .base import *

DOTENV_FILE = REPO_DIR.child('.local.env')
ENV_CONFIG = Config(RepositoryEnv(DOTENV_FILE))

SECRET_KEY = ENV_CONFIG.get('SECRET_KEY')

DEBUG = ENV_CONFIG.get('DEBUG', cast=bool)

ALLOWED_HOSTS = ENV_CONFIG.get('ALLOWED_HOSTS').split(',')


MIDDLEWARE.remove('django.middleware.csrf.CsrfViewMiddleware')

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = REPO_DIR.child('django_sessions')
SESSION_SAVE_EVERY_REQUEST = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': REPO_DIR.child('db.sqlite3'),
    }
}
