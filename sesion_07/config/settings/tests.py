"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

# General
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Passwords
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
