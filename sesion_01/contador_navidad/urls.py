"""Contador Navidad URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path("contador/", include("contador_app.urls")),
]
