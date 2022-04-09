"""Movies app URLs"""

from django.urls import path

from movies import views

app_name = "movies"
urlpatterns = [
    path("", views.list_movies, name="list"),
    path("<int:pk>", views.MovieDetailView.as_view(), name="retrieve"),
    path("director/create", views.create_director_with_normal_form, name="create_director"),
]
