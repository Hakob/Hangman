from .base import *

if 'DJANGO_SECRET_KEY' in os.environ:  # if hasattr(os.environ, 'DJANGO_SECRET_KEY')
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    print('SECRET_KEY value is hardcoded into settings')
    SECRET_KEY = 'phx(0-_u(7-xg-5w28eao0&a5fxh6n47dbszex(5c)6i0mdb4f'

DEBUG = True

ALLOWED_HOSTS = []

MIDDLEWARE.remove('django.middleware.csrf.CsrfViewMiddleware')

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = BASE_DIR + '\\django_sessions'
SESSION_SAVE_EVERY_REQUEST = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
