"""Movies app views tests"""

from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from freezegun import freeze_time

from ..models import Movie, Director


User = get_user_model()


class TestViews(TestCase):
    @classmethod
    def setUpTestData(self):
        self.director = Director.objects.create(
            first_name='Quentin',
            last_name='Tarantino',
            birthday=date(1963, 3, 27),
        )
        self.movie = Movie.objects.create(
            name='Pulp Fiction',
            director=self.director,
            release_date=date(1994, 10, 14),
        )
        self.user = User.objects.create_user(
            username="ultr4nerd",
            first_name="Mau",
            last_name="Chávez Olea",
            password="pass12345",
            email="mauricio@gmail.com"
        )

    def test_list_movies(self):
        self.client.force_login(self.user)
        url = reverse("movies:list")
        response = self.client.get(url)
        self.assertContains(
            response, f"{ self.movie.name } de { self.director.full_name }")

    def test_list_movies__no_auth(self):
        url = reverse("movies:list")
        response = self.client.get(url, follow=True)
        self.assertContains(response, "Iniciar sesión")

    def test_retrieve_movie(self):
        self.client.force_login(self.user)
        url = reverse("movies:retrieve", args=[self.movie.pk])
        response = self.client.get(url)
        self.assertContains(response, self.movie.name)
        self.assertContains(response, self.director.first_name)
        self.assertContains(response, self.director.last_name)

    def test_retrieve_movies__no_auth(self):
        url = reverse("movies:retrieve",  args=[self.movie.pk])
        response = self.client.get(url, follow=True)
        self.assertContains(response, "Iniciar sesión")

    def test_create_director__get(self):
        self.client.force_login(self.user)
        url = reverse("movies:create_director")
        response = self.client.get(url)
        self.assertContains(response, "Crear director")

    @freeze_time("2022-04-09")
    def test_create_director__post(self):
        self.client.force_login(self.user)
        data = {
            "first_name": "Christopher",
            "last_name": "Nolan",
            "birthday": date(1970, 7, 30),
        }

        director_exists = Director.objects.filter(**data).exists()
        self.assertFalse(director_exists)

        url = reverse("movies:create_director")
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        director_exists = Director.objects.filter(**data).exists()
        self.assertTrue(director_exists)

    @freeze_time("1970-07-29")
    def test_create_director__post_with_birthday_error(self):
        self.client.force_login(self.user)
        url = reverse("movies:create_director")
        data = {
            "first_name": "Christopher",
            "last_name": "Nolan",
            "birthday": date(1970, 7, 30),
        }
        response = self.client.post(url, data)
        self.assertContains(response, "El cumpleaños está en el futuro")

    @freeze_time("2022-04-09")
    def test_create_director__post_with_existing_director_error(self):
        data = {
            "first_name": "Christopher",
            "last_name": "Nolan",
            "birthday": date(1970, 7, 30),
        }
        Director.objects.create(**data)

        self.client.force_login(self.user)
        url = reverse("movies:create_director")
        response = self.client.post(url, data)
        self.assertContains(response, "El director ya existe")
