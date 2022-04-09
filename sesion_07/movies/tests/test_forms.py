"""Movies app forms tests"""

from django.test import TestCase

from freezegun import freeze_time

from ..forms import DirectorForm
from ..models import Director


class TestDirectorForm(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Christopher",
            "last_name": "Nolan",
            "birthday": "1970-07-30"
        }
        self.form = DirectorForm(data=self.data)

    @freeze_time("1970-08-01")
    def test_clean_birthday(self):
        self.assertTrue(self.form.is_valid())
        self.assertNotIn('birthday', self.form.errors)

    @freeze_time("1970-07-29")
    def test_clean_birthday__birthday_in_future(self):
        self.assertFalse(self.form.is_valid())
        self.assertIn('birthday', self.form.errors)
        self.assertIn(
            'El cumpleaños está en el futuro',
            self.form.errors['birthday']
        )
        self.assertEqual(len(self.form.errors['birthday']), 1)

    @freeze_time("2022-04-09")
    def test_clean(self):
        self.assertTrue(self.form.is_valid())

    @freeze_time("2022-04-09")
    def test_clean(self):
        Director.objects.create(**self.data)
        self.assertFalse(self.form.is_valid())
        self.assertIn('El director ya existe', self.form.non_field_errors())
        self.assertEqual(len(self.form.non_field_errors()), 1)

    @freeze_time("2022-04-09")
    def test_save(self):
        director_exists = Director.objects.filter(**self.data).exists()
        self.assertFalse(director_exists)
        self.assertTrue(self.form.is_valid())
        self.form.save()
        director_exists = Director.objects.filter(**self.data).exists()
        self.assertTrue(director_exists)
