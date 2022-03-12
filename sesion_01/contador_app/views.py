"""Contador app view"""

import random

from django.shortcuts import render


def hola_mundo(request):
    context = {
        "mi_numero": random.randint(0, 10),
        "lista_compras": ["Zanahoria", "Leche", "Pastel"]
    }
    return render(request, "index.html", context)
