from .base import *


if 'DJANGO_SECRET_KEY' in os.environ:
	SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
	print('SECRET_KEY value is hardcoded into settings')
	SECRET_KEY = '5w28vnidfphx(0-_u(7-xg-vdivja5fxh6n47dbszex(5c)6i0mdb4f'


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


SESSION_ENGINE = 'django.contrib.sessions.backends.db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
        }
    }
}
