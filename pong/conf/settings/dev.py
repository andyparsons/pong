"""Development settings and globals."""
from common import *

"""Production settings and globals."""
from common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'pong',
        'USER': 'dev_user',
        'PASSWORD': 'dev_password',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
}