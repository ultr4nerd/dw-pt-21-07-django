"""Rotten Tomatoes URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("reviews.urls")),
    path("movies/", include("movies.urls")),
    path("auth/", include("users.urls")),
]
