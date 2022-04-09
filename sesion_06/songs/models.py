"""Songs app models"""

from django.db import models

from core.models import TimestampedModel


class Artist(TimestampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name', ]

    def __str__(self) -> str:
        return self.name


class Album(TimestampedModel):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)

    class Meta:
        ordering = ['title', ]

    def __str__(self) -> str:
        return self.title


class Song(TimestampedModel):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)

    class Meta:
        ordering = ['title', ]

    def __str__(self) -> str:
        return self.title
