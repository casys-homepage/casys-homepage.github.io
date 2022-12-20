"""
WSGI config for calab project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys
sys.path.append('/home/lab/calab_django')
sys.path.append('C:\\Users\\wskwak\\CloudStation\\Dropbox\\documents\\workspace\\django\\calab_django')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calab.settings")

application = get_wsgi_application()
