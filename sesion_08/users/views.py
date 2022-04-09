"""Users app views"""

from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as generic_views

from .forms import SignupForm


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
