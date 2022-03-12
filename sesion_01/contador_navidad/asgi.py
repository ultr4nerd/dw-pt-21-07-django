"""ASGI config for contador_navidad project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contador_navidad.settings')

application = get_asgi_application()
