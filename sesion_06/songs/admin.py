"""Songs app admin site"""

from django.contrib import admin

from .models import Song, Artist, Album


admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
