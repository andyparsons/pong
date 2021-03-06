"""

Django settings for pong project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../.."),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jir#-)3r21%(c@4oa7_y+2z6*!zs457tjqlp=9h)rp(2_z27&j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
)

THIRD_PARTY_APPS = (
    'south',
    'django_extensions',
    'rest_framework',
    'django_assets',
)

LOCAL_APPS = (
    'account',
    'help',
    'assets',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pong.urls'

WSGI_APPLICATION = 'pong.wsgi.application'

TEMPLATE_LOADERS = (
    'djaml.loaders.DjamlFilesystemLoader',
    'djaml.loaders.DjamlAppDirectoriesLoader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

BOWER_COMPONENTS_ROOT = PROJECT_ROOT

BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
    'bower-foundation',
    'font-awesome',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'djangobower.finders.BowerFinder',
)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
#STATICFILES_DIRS = (
#    os.path.join(PROJECT_ROOT, 'static'),
#)

# Pipline for assets
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_SASS_BINARY = '/usr/bin/sass'

PIPELINE_CSS = {
    'app': {
        'source_filenames': (
          'static/bower-foundation/css/*',
        ),
        'output_filename': 'css/app1.css',
    },
}

PIPELINE_JS = {
    'app': {
        'source_filenames': (
          'js/*.js',
        ),
        'output_filename': 'bower_components/js/app.js',
    }
}

AUTH_PROFILE_MODULE = "account.UserProfile"

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
