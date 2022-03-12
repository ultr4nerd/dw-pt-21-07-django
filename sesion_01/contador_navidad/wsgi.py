"""WSGI config for contador_navidad project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contador_navidad.settings')

application = get_wsgi_application()
