"""Songs app models"""

from django.db import models


class Artist(models.Model):
    """Artist model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Album(models.Model):
    """Album model"""
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="covers/")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Song(models.Model):
    """Song model"""
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
