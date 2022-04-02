"""Movies views"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic as generic_views

from .forms import DirectorForm, DirectorModelForm
from .models import Movie

# Class-based views


class MovieDetailView(LoginRequiredMixin, generic_views.DetailView):
    model = Movie


# Function-based views

@login_required
def list_movies(request):
    movies = Movie.objects.all()

    for movie in movies:
        movie.reviewed = movie.has_user_review(request.user)

    context = {"movies": movies}
    return render(request, "movies/list.html", context)


@login_required
def retrieve_movie_full(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        context = {"movie": movie}
        return render(request, "movies/retrieve.html", context)
    except Movie.DoesNotExist:
        raise Http404


@login_required
def retrieve_movie_shortcut(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {"movie": movie}
    return render(request, "movies/retrieve.html", context)


@login_required
def create_director_with_normal_form(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    return render(request, "movies/create_director.html", {"form": form})


@login_required
def create_director_with_model_form(request):
    form = DirectorModelForm()
    if request.method == 'POST':
        form = DirectorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    return render(request, "movies/create_director.html", {"form": form})
