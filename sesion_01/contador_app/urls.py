"""Contador app URL's"""

from django.urls import path

from .views import hola_mundo, contador

app_name = 'contador'

urlpatterns = [
    path("hola_mundo/", hola_mundo),
    path("contador/", contador),
]
