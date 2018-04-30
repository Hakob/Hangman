from decouple import Config, RepositoryEnv

from .base import *

DOTENV_FILE = REPO_DIR.child('prod.env')
ENV_CONFIG = Config(RepositoryEnv(DOTENV_FILE))

SECRET_KEY = ENV_CONFIG.get('SECRET_KEY')

DEBUG = ENV_CONFIG.get('DEBUG', cast=bool)

ALLOWED_HOSTS = ENV_CONFIG.get('ALLOWED_HOSTS').split(',')


SESSION_ENGINE = 'django.contrib.sessions.backends.db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': REPO_DIR.child('my.cnf'),
        }
    }
}
