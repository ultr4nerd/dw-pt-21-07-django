"""Core app models"""

from django.db import models


class TimestampedModel(models.Model):
    """This model is for creating other models, do not use it directly"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
