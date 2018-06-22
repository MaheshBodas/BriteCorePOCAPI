"""
WSGI config for heroku_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'BriteCorePOCAPI.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BriteCorePOCAPI.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)