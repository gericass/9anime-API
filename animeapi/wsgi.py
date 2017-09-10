"""
WSGI config for animeapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import api.resident as logger
import time
import threading


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animeapi.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise



application = get_wsgi_application()
application = DjangoWhiteNoise(application)


t = threading.Thread(target=logger.process)
t.start()
