"""
WSGI config for django_web_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

import sys

from pathlib import Path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web_app.settings')

sys.path.append('C:/Users/kimat/Desktop/projects/django_web_app/django_web_app')

application = get_wsgi_application()
