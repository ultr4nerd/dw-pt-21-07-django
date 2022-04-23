from django.contrib.auth import get_user_model
from django.db import models


class Address(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    zip_code = models.PositiveIntegerField()
    suburb = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return f"({self.latitude}, {self.longitude})"
