# Local overrides for any config go here

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'pong',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
}