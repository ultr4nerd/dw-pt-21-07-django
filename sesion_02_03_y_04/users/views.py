"""Users app views"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from .forms import SignupForm

# Vistas basadas en clases | Class based views | CBV


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"


class SignupView(generic_views.FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("reviews:list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# Vistas basadas en funciones | Function based views | FBV

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect("movies:list")
        else:
            context["error"] = "Credenciales incorrectas"
    return render(request, "users/login.html", context)


def user_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("movies:list")
    return render(request, "users/signup.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("users:login")
