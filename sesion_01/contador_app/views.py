"""Contador app view"""

import random
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render


def hola_mundo(request):
    context = {
        "mi_numero": random.randint(0, 10),
        "lista_compras": ["Zanahoria", "Leche", "Pastel"]
    }
    return render(request, "contador_app/index.html", context)


def contador(request):
    """Cuenta los días que faltan para navidad"""
    now = date.today()
    if now.month == 12 and now.day > 25:
        christmas = date(now.year + 1, 12, 25)
    else:
        christmas = date(now.year, 12, 25)
    days_until_christmas = (christmas - now).days

    if days_until_christmas == 0:
        message = "¡Ya es navidad!"
    elif days_until_christmas == 1:
        message = "Falta 1 día para navidad"
    else:
        message = f"Faltan {days_until_christmas} días para navidad"

    return HttpResponse(message)
