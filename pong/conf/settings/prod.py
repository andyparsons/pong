"""Production settings and globals."""
from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'pong',
        'USER': 'prod_user',
        'PASSWORD': 'prod_password',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
}