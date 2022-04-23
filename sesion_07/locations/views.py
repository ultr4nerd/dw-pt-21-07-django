"""Locations app views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, RedirectView

from .forms import AddressForm
from .models import Address


class CreateAddressView(LoginRequiredMixin, FormView):
    form_class = AddressForm
    template_name = "locations/create-address.html"
    success_url = reverse_lazy("locations:show")

    def form_valid(self, form):
        user = self.request.user
        queryset = Address.objects.filter(user=user)
        if queryset.exists():
            queryset.delete()

        address = form.save(commit=False)
        address.user = user
        address.save()
        return super().form_valid(form)


class ShowUserAddressView(LoginRequiredMixin, TemplateView):
    template_name = "locations/show-address.html"


class DeleteAddressView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy("locations:show")

    def get_redirect_url(self, *args, **kwargs):
        address = get_object_or_404(Address, user=self.request.user)
        address.delete()
        return super().get_redirect_url(*args, **kwargs)
