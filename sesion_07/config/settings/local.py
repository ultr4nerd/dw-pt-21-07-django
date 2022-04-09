from .base import *
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)
DEBUG = True
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Django Extensions
INSTALLED_APPS += ["django_extensions"]  # noqa F405
