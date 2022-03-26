"""Movies app models"""

from django.db import models

from reviews.models import Review


class Movie(models.Model):
    """Movie model for movies app"""
    name = models.CharField(max_length=255)
    director = models.ForeignKey("Director", on_delete=models.CASCADE)
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def has_user_review(self, user):
        return Review.objects.filter(movie=self, user=user).exists()


class Director(models.Model):
    """Director of a movie"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
