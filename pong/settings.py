import os
import sys, traceback

## Import our defaults (globals)

from pong.conf.settings.default import *

## Inherit from environment specifics

DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), locals(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

## Import local settings

try:
    from conf.settings.local import *
    sys.stdout.write("Using local settings from conf/settings/local.py\n")
except ImportError:
    sys.stderr.write("Warning: Can't find the file 'local.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()